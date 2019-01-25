"""TheFunctionWithin"""

def main(numa, numb, numc, numd):
    """Function process and print"""
    print(varf(varf(numa)))
    print(varg(varf(numa-numb)))
    print(varh(varf(numa+numb), varf(numa+numc), varg(varf(numd**2))))
    para1 = varh(varf(numa+numb), varf(numa-numc), varg(varf(numd**2)))
    para2 = varg(varf(numa-numb))
    para3 = varf(varf(varf(varf(varf(numc)))))
    print(vari(para1, para2, para3, numd**8))

def varf(numx):
    """function_f"""
    return 2*numx

def varg(numx):
    """function_g"""
    return 3*numx**4-numx**3+2*numx**2+10

def varh(numx, numy, numz):
    """function_h"""
    return (numz+numx)**2-numx*numy+numy**2

def vari(numa, numb, numc, numd):
    """function_i"""
    return (numa**2+numb**2-numc**2)/(numd**2-2*numa*numd+2*numa)

main(float(input()), float(input()), float(input()), float(input()))
