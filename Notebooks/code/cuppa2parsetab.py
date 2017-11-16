
# cuppa2parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftEQLEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTPLUS MINUS TIMES DIVIDE EQ LE INTEGER ID GET PUT IF ELSE WHILE NOT DECLARE\n    program : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | empty\n    \n    stmt : DECLARE ID opt_init opt_semi\n         | ID '=' exp opt_semi\n         | GET ID opt_semi\n         | PUT exp opt_semi\n         | WHILE '(' exp ')' stmt\n         | IF '(' exp ')' stmt opt_else\n         | '{' stmt_list '}'\n    \n    opt_init : '=' exp\n             | empty\n    \n    opt_else : ELSE stmt\n             | empty\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp EQ exp\n        | exp LE exp\n    \n    exp : INTEGER\n    \n    exp : ID\n    \n    exp : '(' exp ')'\n    \n    exp : MINUS exp %prec UMINUS\n    \n    exp : NOT exp\n    \n    opt_semi : ';'\n             | empty\n    \n    empty :\n    "
    
_lr_action_items = {'DECLARE':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[5,5,5,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,5,5,-8,-28,-9,5,-14,-13,]),'ID':([0,3,5,7,8,11,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[6,6,13,15,19,6,-28,19,-28,-28,19,-21,-22,19,19,19,19,-28,19,-12,-28,-6,-26,-27,-7,19,19,19,19,19,19,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,6,6,-8,-28,-9,6,-14,-13,]),'GET':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[7,7,7,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,7,7,-8,-28,-9,7,-14,-13,]),'PUT':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[8,8,8,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,8,8,-8,-28,-9,8,-14,-13,]),'WHILE':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[9,9,9,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,9,9,-8,-28,-9,9,-14,-13,]),'IF':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[10,10,10,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,10,10,-8,-28,-9,10,-14,-13,]),'{':([0,3,11,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,],[11,11,11,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,11,11,-8,-28,-9,11,-14,-13,]),'$end':([0,1,2,3,4,12,13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,57,58,59,61,62,],[-28,0,-1,-28,-3,-2,-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,-8,-28,-9,-14,-13,]),'}':([3,4,11,12,13,15,16,18,19,24,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,57,58,59,61,62,],[-28,-3,-28,-2,-28,-28,-28,-21,-22,44,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,-8,-28,-9,-14,-13,]),'=':([6,13,],[14,26,]),'INTEGER':([8,14,17,20,21,22,23,26,33,34,35,36,37,38,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'(':([8,9,10,14,17,20,21,22,23,26,33,34,35,36,37,38,],[20,22,23,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'MINUS':([8,14,16,17,18,19,20,21,22,23,26,28,33,34,35,36,37,38,39,40,41,42,43,46,48,49,50,51,52,53,54,],[17,17,34,17,-21,-22,17,17,17,17,17,34,17,17,17,17,17,17,-24,34,-25,34,34,34,-15,-16,-17,-18,34,34,-23,]),'NOT':([8,14,17,20,21,22,23,26,33,34,35,36,37,38,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),';':([13,15,16,18,19,25,27,28,39,41,46,48,49,50,51,52,53,54,],[-28,30,30,-21,-22,30,-12,30,-24,-25,-11,-15,-16,-17,-18,-19,-20,-23,]),'ELSE':([13,15,16,18,19,25,27,28,29,30,31,32,39,41,44,45,46,47,48,49,50,51,52,53,54,57,58,59,61,62,],[-28,-28,-28,-21,-22,-28,-12,-28,-6,-26,-27,-7,-24,-25,-10,-4,-11,-5,-15,-16,-17,-18,-19,-20,-23,-8,60,-9,-14,-13,]),'PLUS':([16,18,19,28,39,40,41,42,43,46,48,49,50,51,52,53,54,],[33,-21,-22,33,-24,33,-25,33,33,33,-15,-16,-17,-18,33,33,-23,]),'TIMES':([16,18,19,28,39,40,41,42,43,46,48,49,50,51,52,53,54,],[35,-21,-22,35,-24,35,-25,35,35,35,35,35,-17,-18,35,35,-23,]),'DIVIDE':([16,18,19,28,39,40,41,42,43,46,48,49,50,51,52,53,54,],[36,-21,-22,36,-24,36,-25,36,36,36,36,36,-17,-18,36,36,-23,]),'EQ':([16,18,19,28,39,40,41,42,43,46,48,49,50,51,52,53,54,],[37,-21,-22,37,-24,37,-25,37,37,37,-15,-16,-17,-18,-19,-20,-23,]),'LE':([16,18,19,28,39,40,41,42,43,46,48,49,50,51,52,53,54,],[38,-21,-22,38,-24,38,-25,38,38,38,-15,-16,-17,-18,-19,-20,-23,]),')':([18,19,39,40,41,42,43,48,49,50,51,52,53,54,],[-21,-22,-24,54,-25,55,56,-15,-16,-17,-18,-19,-20,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,3,11,],[2,12,24,]),'stmt':([0,3,11,55,56,60,],[3,3,3,57,58,62,]),'empty':([0,3,11,13,15,16,25,28,58,],[4,4,4,27,31,31,31,31,61,]),'exp':([8,14,17,20,21,22,23,26,33,34,35,36,37,38,],[16,28,39,40,41,42,43,46,48,49,50,51,52,53,]),'opt_init':([13,],[25,]),'opt_semi':([15,16,25,28,],[29,32,45,47,]),'opt_else':([58,],[59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_prog','cuppa2_frontend_gram.py',23),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','cuppa2_frontend_gram.py',30),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','cuppa2_frontend_gram.py',31),
  ('stmt -> DECLARE ID opt_init opt_semi','stmt',4,'p_stmt','cuppa2_frontend_gram.py',41),
  ('stmt -> ID = exp opt_semi','stmt',4,'p_stmt','cuppa2_frontend_gram.py',42),
  ('stmt -> GET ID opt_semi','stmt',3,'p_stmt','cuppa2_frontend_gram.py',43),
  ('stmt -> PUT exp opt_semi','stmt',3,'p_stmt','cuppa2_frontend_gram.py',44),
  ('stmt -> WHILE ( exp ) stmt','stmt',5,'p_stmt','cuppa2_frontend_gram.py',45),
  ('stmt -> IF ( exp ) stmt opt_else','stmt',6,'p_stmt','cuppa2_frontend_gram.py',46),
  ('stmt -> { stmt_list }','stmt',3,'p_stmt','cuppa2_frontend_gram.py',47),
  ('opt_init -> = exp','opt_init',2,'p_opt_init','cuppa2_frontend_gram.py',69),
  ('opt_init -> empty','opt_init',1,'p_opt_init','cuppa2_frontend_gram.py',70),
  ('opt_else -> ELSE stmt','opt_else',2,'p_opt_else','cuppa2_frontend_gram.py',80),
  ('opt_else -> empty','opt_else',1,'p_opt_else','cuppa2_frontend_gram.py',81),
  ('exp -> exp PLUS exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',91),
  ('exp -> exp MINUS exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',92),
  ('exp -> exp TIMES exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',93),
  ('exp -> exp DIVIDE exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',94),
  ('exp -> exp EQ exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',95),
  ('exp -> exp LE exp','exp',3,'p_binop_exp','cuppa2_frontend_gram.py',96),
  ('exp -> INTEGER','exp',1,'p_integer_exp','cuppa2_frontend_gram.py',103),
  ('exp -> ID','exp',1,'p_id_exp','cuppa2_frontend_gram.py',110),
  ('exp -> ( exp )','exp',3,'p_paren_exp','cuppa2_frontend_gram.py',117),
  ('exp -> MINUS exp','exp',2,'p_uminus_exp','cuppa2_frontend_gram.py',124),
  ('exp -> NOT exp','exp',2,'p_not_exp','cuppa2_frontend_gram.py',131),
  ('opt_semi -> ;','opt_semi',1,'p_opt_semi','cuppa2_frontend_gram.py',138),
  ('opt_semi -> empty','opt_semi',1,'p_opt_semi','cuppa2_frontend_gram.py',139),
  ('empty -> <empty>','empty',0,'p_empty','cuppa2_frontend_gram.py',146),
]