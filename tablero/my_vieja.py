import sys
import math

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    Q = int(input_data[ptr]); ptr += 1
    

    mat = []
    for i in range(N):
        row = [int(x) for x in input_data[ptr : ptr + N]]
        mat.append(row)
        ptr += N
        
   
    output = []
    while ptr < len(input_data):
        tipo = input_data[ptr]; ptr += 1
        
        if tipo == 'U':
            r = int(input_data[ptr]) - 1; ptr += 1
            c = int(input_data[ptr]) - 1; ptr += 1
            val = int(input_data[ptr]); ptr += 1
            mat[r][c] = val
            
        elif tipo == 'Q':
            r1 = int(input_data[ptr]) - 1; ptr += 1
            c1 = int(input_data[ptr]) - 1; ptr += 1
            r2 = int(input_data[ptr]) - 1; ptr += 1
            c2 = int(input_data[ptr]) - 1; ptr += 1
            
            curr_max = -float('inf')
            curr_min = float('inf')
            
            
            for i in range(r1, r2 + 1):
                sub_fila = mat[i][c1 : c2 + 1]
                local_max = max(sub_fila)
                local_min = min(sub_fila)
                
                if local_max > curr_max: curr_max = local_max
                if local_min < curr_min: curr_min = local_min
            
            output.append(str(curr_max - curr_min))

    # Escribir todo de una sola vez
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()