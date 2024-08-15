def get_size(w,h,l):
    volume = l * w * h
    sa = 2*(l*w) + 2*(w*h) + 2*(l*h)
    return[sa,volume]