
def minimum(scalar_values):
    minimum=scalar_values[0]
    for i in scalar_values:
        if i<minimum:
            minimum=i

    return (minimum)

scalar_values=[24,-16]

minimum(scalar_values)
