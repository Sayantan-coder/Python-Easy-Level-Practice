def calculate_damage(damage, speed, time):
    if time not in ["second", "minute", "hour"]:
        raise ValueError("Invalide Time!Time must be in second,minute,hour")
    else:
        net_damage = damage * speed
        if time == "second":
            return net_damage
        elif time == "minute":
            return net_damage * 60
        else:
            return net_damage * 3600


damage_calculation = calculate_damage(30, 6, "minute")
print(damage_calculation)
