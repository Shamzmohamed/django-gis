from django.core.management.base import BaseCommand
from django.db.models import Q, Count, Sum
from wildlife.models import *

class Command(BaseCommand):
    help = "Run Wildlife ORM"

    def function_1(self):
        """Get properties by type"""
        print("1. Get properties by type")
        # implement your code
        properties = Property.objects.filter(property_type__name__in=['Private', 'Community'])
        for p in properties:
            print(f"- {p.name} ({p.property_type.name})")

    def function_2(self):
        """Get provinces with organisations or properties"""
        print("2. Get provinces with organisations or properties")
        # implement your code
        provinces = Province.objects.filter(
            Q(organisation__isnull=False) | Q(property__isnull=False)
        ).distinct()
        for province in provinces:
            print(f"- {province.name}")

    def function_3(self):
        """Organisation and property count per province"""
        print("\n3. Organisation and property count per province")

        provinces = Province.objects.annotate(
            org_count=Count("organisation", distinct=True),
            prop_count=Count("property", distinct=True)
        ).filter(Q(org_count__gt=0) | Q(prop_count__gt=0))

        for p in provinces:
            print(f"{p.name}: {p.org_count} organisations, {p.prop_count} properties")

    def function_4(self):
        """Annual population for Acinonyx jubatus (Cheetah) in 2021"""
        print("\n4. Annual population for Acinonyx jubatus (2021)")
        data = AnnualPopulation.objects.filter(
            taxon__scientific_name__iexact="Acinonyx jubatus",
            year=2021
        ).aggregate(
            males=Sum("adult_male"),
            females=Sum("adult_female")
        )
        print(data)

    def function_5(self):
        """Distinct species count for 'Zakki Property'"""
        print("\n5. Distinct species count for 'Zakki Property'")
        result = AnnualPopulation.objects.filter(
            property__name="Zakki Property"
        ).values("taxon").distinct().count()
        print(f"Distinct species: {result}")

    def function_6(self):
        """Organisation with largest total area available to species"""
        print("\n6. Organisation with largest total area")
        org = Organisation.objects.annotate(
            total_area=Sum("property__annualpopulation__area_available_to_species")
        ).order_by("-total_area").first()
        if org:
            print(f"{org.name}: {org.total_area:.2f} area units")
        else:
            print("No data")

    def function_7(self):
        """Property with most varying (distinct) species"""
        print("\n7. Property with most varying species")
        prop = Property.objects.annotate(
            unique_species=Count("annualpopulation__taxon", distinct=True)
        ).order_by("-unique_species").first()
        if prop:
            print(f"{prop.name}: {prop.unique_species} unique species")
        else:
            print("No data")

    def function_8(self):
        """Property with highest total animal count"""
        print("\n8. Property with highest total animal count")
        prop = Property.objects.annotate(
            total_animals=Sum("annualpopulation__total")
        ).order_by("-total_animals").first()
        if prop:
            print(f"{prop.name}: {prop.total_animals} total animals")
        else:
            print("No data")

    def function_9(self):
        """Province with highest adult male count"""
        print("\n9. Province with highest adult male count")
        prov = Province.objects.annotate(
            total_males=Sum("property__annualpopulation__adult_male")
        ).order_by("-total_males").first()
        if prov:
            print(f"{prov.name}: {prov.total_males} adult males")
        else:
            print("No data")

    def function_10(self):
        """Taxon parent and child taxon"""
        print("\n10. Taxon parent and child taxa for 'Acinonyx jubatus'")
        taxon = Taxon.objects.filter(scientific_name="Acinonyx jubatus").first()
        if taxon:
            print(f"Parent: {taxon.parent}")
            children = Taxon.objects.filter(parent=taxon)
            print("Children:", [c.scientific_name for c in children])
        else:
            print("Taxon not found")

    def function_11(self):
        """Taxa without children"""
        print("\n11. Taxa without children")
        taxa = Taxon.objects.filter(taxon__isnull=True)
        for t in taxa:
            print("-", t.scientific_name)

    def function_12(self):
        """Top user by Annual Population records"""
        print("\n12. Top user by Annual Population records")
        user = User.objects.annotate(
            record_count=Count("annualpopulation")
        ).order_by("-record_count").first()
        if user:
            print(f"{user.username}: {user.record_count} records")
        else:
            print("No users with records")

    def handle(self, *args, **options):
        """Logic of the command"""
        self.function_1()
        self.function_2()
        self.function_3()
        self.function_4()
        self.function_5()
        self.function_6()
        self.function_7()
        self.function_8()
        self.function_9()
        self.function_10()
        self.function_11()
        self.function_12()
