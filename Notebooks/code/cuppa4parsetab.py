
# cuppa4parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftEQLEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTDIVIDE ELSE EQ FLOAT FLOAT_TYPE GET ID IF INTEGER INTEGER_TYPE LE MINUS NOT PLUS PUT RETURN STRING STRING_TYPE TIMES VOID_TYPE WHILE\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | empty\n    \n    stmt : VOID_TYPE ID '(' opt_formal_args ')' stmt\n    \n    stmt : data_type ID '(' opt_formal_args ')' stmt\n    \n    stmt : data_type ID opt_init opt_semi\n    \n    stmt : ID '=' exp opt_semi\n    \n    stmt : GET ID opt_semi\n    \n    stmt : PUT exp opt_semi\n    \n    stmt : ID '(' opt_actual_args ')' opt_semi\n    \n    stmt : RETURN opt_exp opt_semi\n    \n    stmt : WHILE '(' exp ')' stmt\n    \n    stmt : IF '(' exp ')' stmt opt_else\n    \n    stmt : '{' stmt_list '}'\n    \n    data_type : INTEGER_TYPE\n    \n    data_type : FLOAT_TYPE\n    \n    data_type :  STRING_TYPE\n    \n    opt_formal_args : formal_args\n                    | empty\n    \n    formal_args : data_type ID ',' formal_args\n    \n    formal_args : data_type ID\n    \n    opt_init : '=' exp\n             | empty\n    \n    opt_actual_args : actual_args\n                    | empty\n    \n    actual_args : exp ',' actual_args\n                | exp\n    \n    opt_exp : exp\n            | empty\n    \n    opt_else : ELSE stmt\n             | empty\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp EQ exp\n        | exp LE exp\n    \n    exp : INTEGER\n    \n    exp : FLOAT\n    \n    exp : STRING\n    \n    exp : ID\n    \n    exp : ID '(' opt_actual_args ')'\n    \n    exp : '(' exp ')'\n    \n    exp : MINUS exp %prec UMINUS\n    \n    exp : NOT exp\n    \n    opt_semi : ';'\n             | empty\n    \n    empty :\n    "
    
_lr_action_items = {'VOID_TYPE':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[5,5,-48,5,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,5,5,5,-10,5,-42,-12,-48,-4,-5,-13,5,-31,-30,]),'ID':([0,3,5,7,8,9,10,13,14,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,64,68,69,70,71,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[6,6,18,21,22,28,28,6,-15,-16,-17,28,28,-48,-48,-48,28,-38,-39,-40,-41,28,28,-48,-28,-29,28,28,-48,-48,28,-23,-8,-46,-47,-9,28,28,28,28,28,28,-44,28,-45,-11,-14,86,-7,-48,28,-6,-22,-32,-33,-34,-35,-36,-37,-43,6,6,6,-10,6,-42,-12,-48,-4,-5,-13,6,-31,-30,]),'GET':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[8,8,-48,8,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,8,8,8,-10,8,-42,-12,-48,-4,-5,-13,8,-31,-30,]),'PUT':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[9,9,-48,9,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,9,9,9,-10,9,-42,-12,-48,-4,-5,-13,9,-31,-30,]),'RETURN':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[10,10,-48,10,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,10,10,10,-10,10,-42,-12,-48,-4,-5,-13,10,-31,-30,]),'WHILE':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[11,11,-48,11,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,11,11,11,-10,11,-42,-12,-48,-4,-5,-13,11,-31,-30,]),'IF':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[12,12,-48,12,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,12,12,12,-10,12,-42,-12,-48,-4,-5,-13,12,-31,-30,]),'{':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,95,96,97,98,100,],[13,13,-48,13,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,13,13,13,-10,13,-42,-12,-48,-4,-5,-13,13,-31,-30,]),'$end':([0,1,2,3,4,10,17,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,87,90,91,92,93,95,96,98,100,],[-48,0,-1,-48,-3,-48,-2,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,-10,-42,-12,-48,-4,-5,-13,-31,-30,]),'INTEGER_TYPE':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,37,38,43,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,94,95,96,97,98,100,],[14,14,-48,14,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,14,-48,14,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,14,14,14,-10,14,-42,-12,-48,-4,14,-5,-13,14,-31,-30,]),'FLOAT_TYPE':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,37,38,43,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,94,95,96,97,98,100,],[15,15,-48,15,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,15,-48,15,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,15,15,15,-10,15,-42,-12,-48,-4,15,-5,-13,15,-31,-30,]),'STRING_TYPE':([0,3,10,13,21,22,23,25,26,27,28,31,32,33,37,38,43,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,83,84,85,87,89,90,91,92,93,94,95,96,97,98,100,],[16,16,-48,16,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,16,-48,16,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,16,16,16,-10,16,-42,-12,-48,-4,16,-5,-13,16,-31,-30,]),'}':([3,4,10,13,17,21,22,23,25,26,27,28,31,32,33,36,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,87,90,91,92,93,95,96,98,100,],[-48,-3,-48,-48,-2,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,64,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,-10,-42,-12,-48,-4,-5,-13,-31,-30,]),'=':([6,21,],[19,45,]),'(':([6,9,10,11,12,18,19,20,21,24,28,29,30,34,35,45,51,52,53,54,55,56,58,71,],[20,29,29,34,35,37,29,29,43,29,58,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'INTEGER':([9,10,19,20,24,29,30,34,35,45,51,52,53,54,55,56,58,71,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FLOAT':([9,10,19,20,24,29,30,34,35,45,51,52,53,54,55,56,58,71,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'STRING':([9,10,19,20,24,29,30,34,35,45,51,52,53,54,55,56,58,71,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'MINUS':([9,10,19,20,23,24,25,26,27,28,29,30,32,34,35,38,42,45,51,52,53,54,55,56,57,58,59,60,62,63,71,74,75,76,77,78,79,80,82,90,],[24,24,24,24,52,24,-38,-39,-40,-41,24,24,52,24,24,52,52,24,24,24,24,24,24,24,-44,24,52,-45,52,52,24,52,-32,-33,-34,-35,52,52,-43,-42,]),'NOT':([9,10,19,20,24,29,30,34,35,45,51,52,53,54,55,56,58,71,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),';':([10,21,22,23,25,26,27,28,31,32,33,38,44,46,57,60,70,74,75,76,77,78,79,80,82,90,],[-48,-48,48,48,-38,-39,-40,-41,48,-28,-29,48,48,-23,-44,-45,48,-22,-32,-33,-34,-35,-36,-37,-43,-42,]),'ELSE':([10,21,22,23,25,26,27,28,31,32,33,38,44,46,47,48,49,50,57,60,61,64,69,70,73,74,75,76,77,78,79,80,82,87,90,91,92,93,95,96,98,100,],[-48,-48,-48,-48,-38,-39,-40,-41,-48,-28,-29,-48,-48,-23,-8,-46,-47,-9,-44,-45,-11,-14,-7,-48,-6,-22,-32,-33,-34,-35,-36,-37,-43,-10,-42,-12,97,-4,-5,-13,-31,-30,]),')':([20,25,26,27,28,37,39,40,41,42,43,57,58,59,60,62,63,65,66,67,72,75,76,77,78,79,80,81,82,86,88,90,99,],[-48,-38,-39,-40,-41,-48,70,-24,-25,-27,-48,-44,-48,82,-45,83,84,85,-18,-19,89,-32,-33,-34,-35,-36,-37,90,-43,-21,-26,-42,-20,]),'PLUS':([23,25,26,27,28,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,82,90,],[51,-38,-39,-40,-41,51,51,51,-44,51,-45,51,51,51,-32,-33,-34,-35,51,51,-43,-42,]),'TIMES':([23,25,26,27,28,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,82,90,],[53,-38,-39,-40,-41,53,53,53,-44,53,-45,53,53,53,53,53,-34,-35,53,53,-43,-42,]),'DIVIDE':([23,25,26,27,28,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,82,90,],[54,-38,-39,-40,-41,54,54,54,-44,54,-45,54,54,54,54,54,-34,-35,54,54,-43,-42,]),'EQ':([23,25,26,27,28,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,82,90,],[55,-38,-39,-40,-41,55,55,55,-44,55,-45,55,55,55,-32,-33,-34,-35,-36,-37,-43,-42,]),'LE':([23,25,26,27,28,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,82,90,],[56,-38,-39,-40,-41,56,56,56,-44,56,-45,56,56,56,-32,-33,-34,-35,-36,-37,-43,-42,]),',':([25,26,27,28,42,57,60,75,76,77,78,79,80,82,86,90,],[-38,-39,-40,-41,71,-44,-45,-32,-33,-34,-35,-36,-37,-43,94,-42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,3,13,],[2,17,36,]),'stmt':([0,3,13,83,84,85,89,97,],[3,3,3,91,92,93,95,100,]),'empty':([0,3,10,13,20,21,22,23,31,37,38,43,44,58,70,92,],[4,4,33,4,41,46,49,49,49,67,49,67,49,41,49,98,]),'data_type':([0,3,13,37,43,83,84,85,89,94,97,],[7,7,7,68,68,7,7,7,7,68,7,]),'exp':([9,10,19,20,24,29,30,34,35,45,51,52,53,54,55,56,58,71,],[23,32,38,42,57,59,60,62,63,74,75,76,77,78,79,80,42,42,]),'opt_exp':([10,],[31,]),'opt_actual_args':([20,58,],[39,81,]),'actual_args':([20,58,71,],[40,40,88,]),'opt_init':([21,],[44,]),'opt_semi':([22,23,31,38,44,70,],[47,50,61,69,73,87,]),'opt_formal_args':([37,43,],[65,72,]),'formal_args':([37,43,94,],[66,66,99,]),'opt_else':([92,],[96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_prog','cuppa4_frontend.py',23),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','cuppa4_frontend.py',30),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','cuppa4_frontend.py',31),
  ('stmt -> VOID_TYPE ID ( opt_formal_args ) stmt','stmt',6,'p_stmt_1','cuppa4_frontend.py',53),
  ('stmt -> data_type ID ( opt_formal_args ) stmt','stmt',6,'p_stmt_2','cuppa4_frontend.py',59),
  ('stmt -> data_type ID opt_init opt_semi','stmt',4,'p_stmt_3','cuppa4_frontend.py',65),
  ('stmt -> ID = exp opt_semi','stmt',4,'p_stmt_4','cuppa4_frontend.py',71),
  ('stmt -> GET ID opt_semi','stmt',3,'p_stmt_5','cuppa4_frontend.py',77),
  ('stmt -> PUT exp opt_semi','stmt',3,'p_stmt_6','cuppa4_frontend.py',83),
  ('stmt -> ID ( opt_actual_args ) opt_semi','stmt',5,'p_stmt_7','cuppa4_frontend.py',89),
  ('stmt -> RETURN opt_exp opt_semi','stmt',3,'p_stmt_8','cuppa4_frontend.py',95),
  ('stmt -> WHILE ( exp ) stmt','stmt',5,'p_stmt_9','cuppa4_frontend.py',101),
  ('stmt -> IF ( exp ) stmt opt_else','stmt',6,'p_stmt_10','cuppa4_frontend.py',107),
  ('stmt -> { stmt_list }','stmt',3,'p_stmt_11','cuppa4_frontend.py',113),
  ('data_type -> INTEGER_TYPE','data_type',1,'p_data_type_1','cuppa4_frontend.py',123),
  ('data_type -> FLOAT_TYPE','data_type',1,'p_data_type_2','cuppa4_frontend.py',129),
  ('data_type -> STRING_TYPE','data_type',1,'p_data_type_3','cuppa4_frontend.py',135),
  ('opt_formal_args -> formal_args','opt_formal_args',1,'p_opt_formal_args','cuppa4_frontend.py',142),
  ('opt_formal_args -> empty','opt_formal_args',1,'p_opt_formal_args','cuppa4_frontend.py',143),
  ('formal_args -> data_type ID , formal_args','formal_args',4,'p_formal_args_1','cuppa4_frontend.py',153),
  ('formal_args -> data_type ID','formal_args',2,'p_formal_args_2','cuppa4_frontend.py',159),
  ('opt_init -> = exp','opt_init',2,'p_opt_init','cuppa4_frontend.py',166),
  ('opt_init -> empty','opt_init',1,'p_opt_init','cuppa4_frontend.py',167),
  ('opt_actual_args -> actual_args','opt_actual_args',1,'p_opt_actual_args','cuppa4_frontend.py',177),
  ('opt_actual_args -> empty','opt_actual_args',1,'p_opt_actual_args','cuppa4_frontend.py',178),
  ('actual_args -> exp , actual_args','actual_args',3,'p_actual_args','cuppa4_frontend.py',185),
  ('actual_args -> exp','actual_args',1,'p_actual_args','cuppa4_frontend.py',186),
  ('opt_exp -> exp','opt_exp',1,'p_opt_exp','cuppa4_frontend.py',196),
  ('opt_exp -> empty','opt_exp',1,'p_opt_exp','cuppa4_frontend.py',197),
  ('opt_else -> ELSE stmt','opt_else',2,'p_opt_else','cuppa4_frontend.py',204),
  ('opt_else -> empty','opt_else',1,'p_opt_else','cuppa4_frontend.py',205),
  ('exp -> exp PLUS exp','exp',3,'p_exp_1','cuppa4_frontend.py',230),
  ('exp -> exp MINUS exp','exp',3,'p_exp_1','cuppa4_frontend.py',231),
  ('exp -> exp TIMES exp','exp',3,'p_exp_1','cuppa4_frontend.py',232),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_1','cuppa4_frontend.py',233),
  ('exp -> exp EQ exp','exp',3,'p_exp_1','cuppa4_frontend.py',234),
  ('exp -> exp LE exp','exp',3,'p_exp_1','cuppa4_frontend.py',235),
  ('exp -> INTEGER','exp',1,'p_exp_2','cuppa4_frontend.py',241),
  ('exp -> FLOAT','exp',1,'p_exp_3','cuppa4_frontend.py',247),
  ('exp -> STRING','exp',1,'p_exp_4','cuppa4_frontend.py',253),
  ('exp -> ID','exp',1,'p_exp_5','cuppa4_frontend.py',259),
  ('exp -> ID ( opt_actual_args )','exp',4,'p_exp_6','cuppa4_frontend.py',265),
  ('exp -> ( exp )','exp',3,'p_exp_7','cuppa4_frontend.py',271),
  ('exp -> MINUS exp','exp',2,'p_exp_8','cuppa4_frontend.py',277),
  ('exp -> NOT exp','exp',2,'p_exp_9','cuppa4_frontend.py',283),
  ('opt_semi -> ;','opt_semi',1,'p_opt_semi','cuppa4_frontend.py',290),
  ('opt_semi -> empty','opt_semi',1,'p_opt_semi','cuppa4_frontend.py',291),
  ('empty -> <empty>','empty',0,'p_empty','cuppa4_frontend.py',298),
]
