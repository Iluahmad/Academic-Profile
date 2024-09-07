% This is Mr. Ahmad Ilu's baseline RBC model Workspace!
@#define LOGUTILITY = 1

var
  y     ${Y}$        (long_name='output')
  c     ${C}$        (long_name='consumption')
  k     ${K}$        (long_name='capital')
  l     ${L}$        (long_name='labor')
  a     ${A}$        (long_name='productivity')
  r     ${R}$        (long_name='interest Rate')
  w     ${W}$        (long_name='wage')
  iv    ${I}$        (long_name='investment')
  mc    ${MC}$       (long_name='marginal Costs')
;

model_local_variable
  uc    ${U_t^C}$
  ucp   ${E_t U_{t+1}^C}$
  ul    ${U_t^L}$
  fk    ${f_t^K}$
  fl    ${f_t^L}$
;

varexo
  epsa  ${\varepsilon^A}$   (long_name='Productivity Shock')
;

parameters
  BETA  ${\beta}$  (long_name='Discount Factor')
  DELTA ${\delta}$ (long_name='Depreciation Rate')
  GAMMA ${\gamma}$ (long_name='Consumption Utility Weight')
  PSI   ${\psi}$   (long_name='Labor Disutility Weight')
  @#if LOGUTILITY != 1
  ETAC  ${\eta^C}$ (long_name='Risk Aversion')
  ETAL  ${\eta^L}$ (long_name='Inverse Frisch Elasticity')
  @#endif
  ALPHA ${\alpha}$ (long_name='Output Elasticity of Capital')
  RHOA  ${\rho^A}$ (long_name='Discount Factor')
;

% Parameter calibration
ALPHA = 0.35;
BETA  = 0.99;
DELTA = 0.025;
GAMMA = 1;
PSI   = 1.6;
RHOA  = 0.9;
@#if LOGUTILITY == 0
ETAC  = 2;
ETAL  = 1;
@#endif


model;
%marginal utility of consumption and labor
@#if LOGUTILITY == 1
  #uc  = GAMMA*c^(-1);
  #ucp  = GAMMA*c(+1)^(-1);
  #ul = -PSI*(1-l)^(-1);
@#else
  #uc  = GAMMA*c^(-ETAC);
  #ucp  = GAMMA*c(+1)^(-ETAC);
  #ul = -PSI*(1-l)^(-ETAL);
@#endif

%marginal products of production
#fk = ALPHA*y/k(-1);
#fl = (1-ALPHA)*y/l;

[name='intertemporal optimality (Euler)']
uc = BETA*ucp*(1-DELTA+r(+1));
[name='labor supply']
w = -ul/uc;
[name='capital accumulation']
k = (1-DELTA)*k(-1) + iv;
[name='market clearing']
y = c + iv;
[name='production function']
y = a*k(-1)^ALPHA*l^(1-ALPHA);
[name='marginal costs']
mc = 1;
[name='labor demand']
w = mc*fl;
[name='capital demand']
r = mc*fk;
[name='total factor productivity']
log(a) = RHOA*log(a(-1)) + epsa;
end;



write_latex_definitions;
write_latex_parameter_table;
write_latex_original_model;
%write_latex_dynamic_model;
write_latex_static_model;
collect_latex_files;

if system(['/Library/TeX/texbin/pdflatex -halt-on-error -interaction=batchmode ' M_.fname '_TeX_binder.tex'])
    warning('TeX-File did not compile; you need to compile it manually')
end
