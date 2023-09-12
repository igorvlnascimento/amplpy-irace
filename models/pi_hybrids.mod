# Conjuntos
set F;
set H;
set R;

# Variáveis
var X { f in F, h in H } integer >= 0;
var Y { f in F, h in H, r in R } integer >= 0;

# Parâmetros
param p {f in F, h in H};
param u {f in F};
param a {h in H};
param d {h in H, r in R};
param s {f in F, h in H, r in R};

# Função objetivo
minimize Total_Cost: 
	sum{f in F, h in H} p[f, h] * X[f, h] + 
	sum {f in F, h in H, r in R} s[f, h, r] * Y[f, h, r];
	
# Restrições
subject to Capacity {f in F}: sum {h in H} a[h] * X[f, h] <= u[f];
subject to Demands {h in H, r in R}: sum {f in F} Y[f, h, r] >= d[h, r];
subject to Balance {f in F, h in H}: sum {r in R} Y[f, h, r] <= X[f, h];
