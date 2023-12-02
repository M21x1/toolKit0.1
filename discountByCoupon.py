def money_off(discount, coupon):
    """Returns the final price paid after the discount (float < 0.5) and coupon (int < 40) have been applied."""
    full_price = 100
    discount_diff = 1 - discount
    discounted = full_price * discount_diff
    final_price = discounted - coupon
    print(final_price)
    
money_off(0.2, 5)