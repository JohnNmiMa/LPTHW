class DiscountCalculator(object):
    def calculate(self, total, discount_amount, discount_type):
        if discount_type == 'percent':
            percentage_discount = float(discount_amount) / 100
            discount = float(total) * percentage_discount
        else:
            discount = discount_amount
        return discount

