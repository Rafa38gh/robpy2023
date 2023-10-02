# Meu arquivo de teste

import numpy as np
import RobPy as rp

m = rp.matriz_rotacao_x(30.5 * np.pi / 180)

print(1 - np.linalg.det(m))
