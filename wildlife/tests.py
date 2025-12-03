from django.test import TestCase
from django.contrib.auth.models import User
from wildlife.models import (
    Province, Organisation, PropertyType, Property,
    TaxonRank, Taxon, AnnualPopulation
)
from django.db.models import Q, Count, Sum


class WildlifeORMTests(TestCase):
    def setUp(self):
        """Create all the test data used in the ORM tests."""

        # Users
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")

        # Province
        self.province = Province.objects.create(name="Limpopo")

        # Property Types
        self.type_private = PropertyType.objects.create(name="Private")
        self.type_community = PropertyType.objects.create(name="Community")

        # Organisation
        self.org = Organisation.objects.create(
            name="Zakki Org",
            short_code="ZORG",
            province=self.province
        )

        # Property
        self.property = Property.objects.create(
            name="Zakki Property",
            short_code="ZP01",
            province=self.province,
            property_type=self.type_private,
            organisation=self.org,
            centroid=None
        )

        # Taxon Rank
        self.rank_species = TaxonRank.objects.create(name="Species")
        self.rank_genus = TaxonRank.objects.create(name="Genus")

        # Parent (Genus)
        self.taxon_parent = Taxon.objects.create(
            scientific_name="Acinonyx",
            taxon_rank=self.rank_genus
        )

        # Child (Species)
        self.taxon_child = Taxon.objects.create(
            scientific_name="Acinonyx jubatus",
            taxon_rank=self.rank_species,
            parent=self.taxon_parent
        )

        # Annual Populations
        AnnualPopulation.objects.create(
            year=2021,
            total=20,
            adult_male=8,
            adult_female=12,
            user=self.user1,
            taxon=self.taxon_child,
            property=self.property,
            area_available_to_species=100.0
        )

        # One more record from another user to test counting
        AnnualPopulation.objects.create(
            year=2021,
            total=5,
            adult_male=2,
            adult_female=3,
            user=self.user2,
            taxon=self.taxon_child,
            property=self.property,
            area_available_to_species=50.0
        )

    # ---------------------------------------------------------------
    # 1. Properties by type (Private + Community)
    # ---------------------------------------------------------------
    def test_property_filter_by_type(self):
        props = Property.objects.filter(
            property_type__in=[self.type_private, self.type_community]
        )
        self.assertEqual(props.count(), 1)
        self.assertEqual(props.first().name, "Zakki Property")

    # ---------------------------------------------------------------
    # 2. Provinces with organisations or properties
    # ---------------------------------------------------------------
    def test_provinces_with_organisations_or_properties(self):
        provinces = Province.objects.filter(
            Q(organisation__isnull=False) | Q(property__isnull=False)
        ).distinct()
        self.assertEqual(provinces.count(), 1)
        self.assertEqual(provinces.first().name, "Limpopo")

    # ---------------------------------------------------------------
    # 3. Organisation & property count per province
    # ---------------------------------------------------------------
    def test_org_and_property_count_per_province(self):
        province = Province.objects.annotate(
            org_count=Count("organisation"),
            prop_count=Count("property")
        ).first()

        self.assertEqual(province.org_count, 1)
        self.assertEqual(province.prop_count, 1)

    # ---------------------------------------------------------------
    # 4. Annual population for Acinonyx jubatus
    # ---------------------------------------------------------------
    def test_annual_population_for_cheetah(self):
        totals = AnnualPopulation.objects.filter(
            year=2021,
            taxon__scientific_name="Acinonyx jubatus"
        ).aggregate(
            males=Sum("adult_male"),
            females=Sum("adult_female")
        )

        self.assertEqual(totals["males"], 8 + 2)
        self.assertEqual(totals["females"], 12 + 3)

    # ---------------------------------------------------------------
    # 5. Species count for Zakki Property
    # ---------------------------------------------------------------
    def test_species_count_for_property(self):
        species_count = AnnualPopulation.objects.filter(
            property__name="Zakki Property"
        ).values("taxon").distinct().count()

        self.assertEqual(species_count, 1)

    # ---------------------------------------------------------------
    # 6. Organisation with largest area
    # ---------------------------------------------------------------
    def test_organisation_with_largest_area(self):
        org_area = AnnualPopulation.objects.values(
            "property__organisation__name"
        ).annotate(
            total_area=Sum("area_available_to_species")
        ).order_by("-total_area").first()

        self.assertEqual(org_area["property__organisation__name"], "Zakki Org")
        self.assertEqual(org_area["total_area"], 150.0)

    # ---------------------------------------------------------------
    # 7. Property with highest animal count
    # ---------------------------------------------------------------
    def test_property_highest_animal_count(self):
        result = AnnualPopulation.objects.values(
            "property__name"
        ).annotate(
            total_animals=Sum("total")
        ).order_by("-total_animals").first()

        self.assertEqual(result["property__name"], "Zakki Property")
        self.assertEqual(result["total_animals"], 25)

    # ---------------------------------------------------------------
    # 8. Taxon parent & child
    # ---------------------------------------------------------------
    def test_taxon_parent_and_children(self):
        parent = Taxon.objects.get(scientific_name="Acinonyx")
        children = Taxon.objects.filter(parent=parent)

        self.assertEqual(parent.scientific_name, "Acinonyx")
        self.assertEqual(children.count(), 1)
        self.assertEqual(children.first().scientific_name, "Acinonyx jubatus")

    # ---------------------------------------------------------------
    # 9. User with most annual population records
    # ---------------------------------------------------------------
    def test_top_user_by_population_records(self):
        top_user = AnnualPopulation.objects.values(
            "user__username"
        ).annotate(
            record_count=Count("id")
        ).order_by("-record_count", "user__username").first()

        self.assertIn(top_user["user__username"], ["user1", "user2"])
        self.assertEqual(top_user["record_count"], 1)

    # ---------------------------------------------------------------
    # 10. Edge Case: Province with NO organisations or properties
    # ---------------------------------------------------------------
    def test_province_without_data_not_included(self):
        """Province with no organisation or property should not appear in results."""
        empty_province = Province.objects.create(name="EmptyLand")

        provinces = Province.objects.filter(
            Q(organisation__isnull=False) | Q(property__isnull=False)
        ).distinct()

        self.assertNotIn(empty_province, provinces)
