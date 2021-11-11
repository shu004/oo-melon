"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.tax = tax
        self.order_type = order_type

#35.0999999999994 for 6 Aus Int watermelons
#43.2 for 8 Dome cantaloupe

    def get_total(self):
        """Calculate price, including tax."""
        total = (1 + self.tax) * self.qty * self.base_price
        if self.species == "Christmas melon":
            total *= 1.5
        if self.order_type == "international" and self.qty < 10:
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    base_price = 5
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 0.08, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    base_price = 5
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        # def __init__(self, species, qty, tax, order_type):
        super().__init__(species, qty, 0.17, "international")
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Tax-free inspected melons ordered by the government"""
    base_price = 5

    def __init__(self, species, qty):
        super().__init__(species, qty, 0, "government")

    def marked_inspection(self):
        self.passed_inspection = True
