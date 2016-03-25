def circle (radio1, radio2, radio3):
    """
    The Kiss Precise
    """
    s1 = 1.0/radio1
    s2 = 1.0/radio2
    s3 = 1.0/radio3
    a = s1 + s2 + s3
    b = s1*s1+s2*s2+s3*s3
    from math import sqrt
    s41 = a + sqrt(2*a*a - 2*b)
    s42 = a - sqrt(2*a*a - 2*b)
    radio41 = 1.0/ s41
    radio42 = 1.0/ s42
    return radio41, abs(radio42)
