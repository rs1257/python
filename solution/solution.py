import math

stamp_duty_bands = [
    [125000, 0.00], # up to 125000
    [125000, 0.02], # 125001 - 250000
    [675000, 0.05], # 250001 - 925000
    [575000, 0.1], # 925001 - 1500000
    [math.inf, 0.12] # The rest
]

def calculate_stamp_duty(property_value: int) -> int:
    total_stamp_duty = 0

    for band, percentage in stamp_duty_bands:
        stamp_duty_band = min(band, property_value)
        total_stamp_duty += stamp_duty_band * percentage

        property_value -= stamp_duty_band
        if property_value <= 0:
            break

    return total_stamp_duty
