"""MissionImImpossible"""

def main():
    """input and output"""
    var_a, var_b, var_c, var_d = int(input()), int(input()), int(input()), int(input())
    var_e, var_f, var_g, var_h = int(input()), int(input()), int(input()), int(input())
    var_i, var_j, var_k, var_l = int(input()), int(input()), int(input()), int(input())
    delta = (var_a*var_f*var_k) + (var_b*var_g*var_i) + (var_c*var_e*var_j)
    delta += -(var_i*var_f*var_c) - (var_j*var_g*var_a) - (var_k*var_e*var_b)
    #delta_main is finish
    delta_v = (var_d*var_f*var_k) + (var_b*var_g*var_l) + (var_c*var_h*var_j)
    delta_v += -(var_l*var_f*var_c) - (var_j*var_g*var_d) - (var_k*var_h*var_b)
    print(int(delta_v/delta), end=" ") #x finish
    delta_v = (var_a*var_h*var_k) + (var_d*var_g*var_i) + (var_c*var_e*var_l)
    delta_v += -(var_i*var_h*var_c) - (var_l*var_g*var_a) - (var_k*var_e*var_d)
    print(int(delta_v/delta), end=" ") #y finish
    delta_v = (var_a*var_f*var_l) + (var_b*var_h*var_i) + (var_d*var_e*var_j)
    delta_v += -(var_i*var_f*var_d) - (var_j*var_h*var_a) - (var_l*var_e*var_b)
    print(int(delta_v/delta)) #z finish

main()
