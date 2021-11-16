
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEnonassocRELOP_EQRELOP_NERELOP_GTRELOP_LTRELOP_GERELOP_LEleft+-left*/leftMATRIX_PLUSMATRIX_SUBleftMATRIX_MULMATRIX_DIVrightUMINUSleft'BREAK CONTINUE DIV_ASSIGN DT_FLOAT DT_INTEGER DT_STRING ELSE EYE FOR ID IF MATRIX_DIV MATRIX_MUL MATRIX_PLUS MATRIX_SUB MUL_ASSIGN ONES PLUS_ASSIGN PRINT RELOP_EQ RELOP_GE RELOP_GT RELOP_LE RELOP_LT RELOP_NE RETURN SUB_ASSIGN WHILE ZEROSprogram : instructions_opt\n        empty : \n    instructions_opt : instructions instructions_opt : empty \n        instructions : instructions instruction\n                    | instruction\n    \n        instruction : assignment\n                    | conditional_statement\n                    | print_statement\n                    | jump_statement\n                    | return_statement\n                    | while_loop\n                    | for_loop\n                    | instruction_block\n    \n        instruction_block : '{' instructions '}'\n    \n        assignment : assign_id '=' expression ';'\n                    | assign_id MUL_ASSIGN expression ';'\n                    | assign_id DIV_ASSIGN expression ';'\n                    | assign_id PLUS_ASSIGN expression ';'\n                    | assign_id SUB_ASSIGN expression ';'\n    \n        assign_id : ID\n                  | ID vector\n    expression : expression_binop\n                  | expression_relop\n                  | expression_unary\n                  | matrix_funcs\n                  | constant\n                  | ID\n                  | matrix\n                  | '(' expression ')'\n    expression_binop : expression '+' expression\n                | expression '-' expression\n                | expression '*' expression\n                | expression '/' expression\n                | expression MATRIX_PLUS expression\n                | expression MATRIX_SUB expression\n                | expression MATRIX_MUL expression\n                | expression MATRIX_DIV expression\n    expression_relop : expression RELOP_EQ expression\n                | expression RELOP_GT expression\n                | expression RELOP_LT expression\n                | expression RELOP_GE expression\n                | expression RELOP_LE expression\n                | expression RELOP_NE expression\n    expression_unary : '-' expression %prec UMINUS\n                | expression '\\''\n    \n        matrix_funcs : ZEROS '(' expression_list ')'\n                    | ONES '(' expression_list ')'\n                    | EYE '(' expression_list ')'  \n\n    \n        constant : DT_STRING\n                | number\n    \n        matrix : '[' vectors ']'\n\n     vectors : vector \n                | vectors ',' vector\n    \n        vector : '[' numbers ']'\n    \n        numbers : numbers ',' number \n                | number\n                | empty\n    \n        number : DT_INTEGER \n               | DT_FLOAT\n    \n        conditional_statement : IF '(' expression ')' instruction %prec IFX\n                    | IF '(' expression ')' instruction ELSE instruction\n    \n        jump_statement : BREAK ';'\n                        | CONTINUE ';'\n    \n        return_statement : RETURN ';'\n                        | RETURN expression ';'\n    \n        print_statement : PRINT expression_list ';'\n    \n        expression_list : expression_list ',' expression\n                        | expression\n    \n        while_loop : WHILE '(' expression ')' instruction\n    \n        for_loop : FOR ID '=' range_value ':' range_value instruction\n    \n        range_value : DT_INTEGER \n                    | ID                   \n    "
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,24,50,51,52,65,89,95,96,97,98,99,100,129,134,139,140,],[-2,0,-1,-3,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-5,-63,-64,-65,-67,-66,-15,-16,-17,-18,-19,-20,-61,-70,-62,-71,]),'IF':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[15,15,-6,-7,-8,-9,-10,-11,-12,-13,-14,15,-5,-63,-64,-65,15,-67,-66,-15,-16,-17,-18,-19,-20,15,15,-73,-72,-61,-70,15,15,-62,-71,]),'PRINT':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[16,16,-6,-7,-8,-9,-10,-11,-12,-13,-14,16,-5,-63,-64,-65,16,-67,-66,-15,-16,-17,-18,-19,-20,16,16,-73,-72,-61,-70,16,16,-62,-71,]),'BREAK':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[17,17,-6,-7,-8,-9,-10,-11,-12,-13,-14,17,-5,-63,-64,-65,17,-67,-66,-15,-16,-17,-18,-19,-20,17,17,-73,-72,-61,-70,17,17,-62,-71,]),'CONTINUE':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[18,18,-6,-7,-8,-9,-10,-11,-12,-13,-14,18,-5,-63,-64,-65,18,-67,-66,-15,-16,-17,-18,-19,-20,18,18,-73,-72,-61,-70,18,18,-62,-71,]),'RETURN':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[19,19,-6,-7,-8,-9,-10,-11,-12,-13,-14,19,-5,-63,-64,-65,19,-67,-66,-15,-16,-17,-18,-19,-20,19,19,-73,-72,-61,-70,19,19,-62,-71,]),'WHILE':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[20,20,-6,-7,-8,-9,-10,-11,-12,-13,-14,20,-5,-63,-64,-65,20,-67,-66,-15,-16,-17,-18,-19,-20,20,20,-73,-72,-61,-70,20,20,-62,-71,]),'FOR':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[21,21,-6,-7,-8,-9,-10,-11,-12,-13,-14,21,-5,-63,-64,-65,21,-67,-66,-15,-16,-17,-18,-19,-20,21,21,-73,-72,-61,-70,21,21,-62,-71,]),'{':([0,3,5,6,7,8,9,10,11,12,13,23,24,50,51,52,58,65,89,95,96,97,98,99,100,101,123,124,126,129,134,137,138,139,140,],[23,23,-6,-7,-8,-9,-10,-11,-12,-13,-14,23,-5,-63,-64,-65,23,-67,-66,-15,-16,-17,-18,-19,-20,23,23,-73,-72,-61,-70,23,23,-62,-71,]),'ID':([0,3,5,6,7,8,9,10,11,12,13,16,19,21,23,24,25,26,27,28,29,30,40,41,50,51,52,54,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,89,91,95,96,97,98,99,100,101,123,124,126,129,134,135,137,138,139,140,],[22,22,-6,-7,-8,-9,-10,-11,-12,-13,-14,38,38,55,22,-5,38,38,38,38,38,38,38,38,-63,-64,-65,38,22,-67,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-66,124,-15,-16,-17,-18,-19,-20,22,22,-73,-72,-61,-70,124,22,22,-62,-71,]),'}':([5,6,7,8,9,10,11,12,13,24,50,51,52,58,65,89,95,96,97,98,99,100,129,134,139,140,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-5,-63,-64,-65,95,-67,-66,-15,-16,-17,-18,-19,-20,-61,-70,-62,-71,]),'ELSE':([6,7,8,9,10,11,12,13,50,51,52,65,89,95,96,97,98,99,100,129,134,139,140,],[-7,-8,-9,-10,-11,-12,-13,-14,-63,-64,-65,-67,-66,-15,-16,-17,-18,-19,-20,137,-70,-62,-71,]),'=':([14,22,55,56,127,],[25,-21,91,-22,-55,]),'MUL_ASSIGN':([14,22,56,127,],[26,-21,-22,-55,]),'DIV_ASSIGN':([14,22,56,127,],[27,-21,-22,-55,]),'PLUS_ASSIGN':([14,22,56,127,],[28,-21,-22,-55,]),'SUB_ASSIGN':([14,22,56,127,],[29,-21,-22,-55,]),'(':([15,16,19,20,25,26,27,28,29,30,40,41,42,43,44,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[30,40,40,54,40,40,40,40,40,40,40,40,84,85,86,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'-':([16,19,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,45,46,48,49,53,54,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[41,41,41,41,41,41,41,41,68,-23,-24,-25,-26,-27,-28,-29,41,41,-50,-51,-59,-60,68,41,68,68,68,68,68,68,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-46,68,-45,41,41,41,68,68,-31,-32,-33,-34,-35,-36,-37,-38,68,68,68,68,68,68,-30,-52,-47,-48,-49,]),'ZEROS':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'ONES':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'EYE':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'DT_STRING':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'[':([16,19,22,25,26,27,28,29,30,40,41,47,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,122,],[47,47,57,47,47,47,47,47,47,47,47,57,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,57,]),'DT_INTEGER':([16,19,25,26,27,28,29,30,40,41,54,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,91,128,135,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,126,48,126,]),'DT_FLOAT':([16,19,25,26,27,28,29,30,40,41,54,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,128,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),';':([17,18,19,31,32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,81,83,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[50,51,52,65,-69,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,89,96,97,98,99,100,-46,-45,-68,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-30,-52,-47,-48,-49,]),',':([31,32,33,34,35,36,37,38,39,45,46,48,49,57,81,83,87,88,92,93,94,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,127,130,131,132,133,136,],[66,-69,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,-2,-46,-45,122,-53,128,-57,-58,-68,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-30,66,66,66,-52,-55,-47,-48,-49,-54,-56,]),')':([32,33,34,35,36,37,38,39,45,46,48,49,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,131,132,],[-69,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,101,-46,117,-45,123,-68,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-30,130,131,132,-52,-47,-48,-49,]),'+':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[67,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,67,67,67,67,67,67,67,-46,67,-45,67,67,-31,-32,-33,-34,-35,-36,-37,-38,67,67,67,67,67,67,-30,-52,-47,-48,-49,]),'*':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[69,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,69,69,69,69,69,69,69,-46,69,-45,69,69,69,69,-33,-34,-35,-36,-37,-38,69,69,69,69,69,69,-30,-52,-47,-48,-49,]),'/':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[70,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,70,70,70,70,70,70,70,-46,70,-45,70,70,70,70,-33,-34,-35,-36,-37,-38,70,70,70,70,70,70,-30,-52,-47,-48,-49,]),'MATRIX_PLUS':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[71,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,71,71,71,71,71,71,71,-46,71,-45,71,71,71,71,71,71,-35,-36,-37,-38,71,71,71,71,71,71,-30,-52,-47,-48,-49,]),'MATRIX_SUB':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[72,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,72,72,72,72,72,72,72,-46,72,-45,72,72,72,72,72,72,-35,-36,-37,-38,72,72,72,72,72,72,-30,-52,-47,-48,-49,]),'MATRIX_MUL':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[73,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,73,73,73,73,73,73,73,-46,73,-45,73,73,73,73,73,73,73,73,-37,-38,73,73,73,73,73,73,-30,-52,-47,-48,-49,]),'MATRIX_DIV':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[74,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,74,74,74,74,74,74,74,-46,74,-45,74,74,74,74,74,74,74,74,-37,-38,74,74,74,74,74,74,-30,-52,-47,-48,-49,]),'RELOP_EQ':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[75,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,75,75,75,75,75,75,75,-46,75,-45,75,75,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),'RELOP_GT':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[76,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,76,76,76,76,76,76,76,-46,76,-45,76,76,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),'RELOP_LT':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[77,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,77,77,77,77,77,77,77,-46,77,-45,77,77,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),'RELOP_GE':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[78,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,78,78,78,78,78,78,78,-46,78,-45,78,78,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),'RELOP_LE':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[79,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,79,79,79,79,79,79,79,-46,79,-45,79,79,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),'RELOP_NE':([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[80,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,80,80,80,80,80,80,80,-46,80,-45,80,80,-31,-32,-33,-34,-35,-36,-37,-38,None,None,None,None,None,None,-30,-52,-47,-48,-49,]),"'":([32,33,34,35,36,37,38,39,45,46,48,49,53,59,60,61,62,63,64,81,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,121,130,131,132,],[81,-23,-24,-25,-26,-27,-28,-29,-50,-51,-59,-60,81,81,81,81,81,81,81,-46,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,-30,-52,-47,-48,-49,]),']':([48,49,57,87,88,92,93,94,127,133,136,],[-59,-60,-2,121,-53,127,-57,-58,-55,-54,-56,]),':':([124,125,126,],[-73,135,-72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,23,],[3,58,]),'empty':([0,57,],[4,94,]),'instruction':([0,3,23,58,101,123,137,138,],[5,24,5,24,129,134,139,140,]),'assignment':([0,3,23,58,101,123,137,138,],[6,6,6,6,6,6,6,6,]),'conditional_statement':([0,3,23,58,101,123,137,138,],[7,7,7,7,7,7,7,7,]),'print_statement':([0,3,23,58,101,123,137,138,],[8,8,8,8,8,8,8,8,]),'jump_statement':([0,3,23,58,101,123,137,138,],[9,9,9,9,9,9,9,9,]),'return_statement':([0,3,23,58,101,123,137,138,],[10,10,10,10,10,10,10,10,]),'while_loop':([0,3,23,58,101,123,137,138,],[11,11,11,11,11,11,11,11,]),'for_loop':([0,3,23,58,101,123,137,138,],[12,12,12,12,12,12,12,12,]),'instruction_block':([0,3,23,58,101,123,137,138,],[13,13,13,13,13,13,13,13,]),'assign_id':([0,3,23,58,101,123,137,138,],[14,14,14,14,14,14,14,14,]),'expression_list':([16,84,85,86,],[31,118,119,120,]),'expression':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[32,53,59,60,61,62,63,64,82,83,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,32,32,32,]),'expression_binop':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'expression_relop':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'expression_unary':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'matrix_funcs':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'constant':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'matrix':([16,19,25,26,27,28,29,30,40,41,54,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'number':([16,19,25,26,27,28,29,30,40,41,54,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,128,],[46,46,46,46,46,46,46,46,46,46,46,93,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,136,]),'vector':([22,47,122,],[56,88,133,]),'vectors':([47,],[87,]),'numbers':([57,],[92,]),'range_value':([91,135,],[125,138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',31),
  ('empty -> <empty>','empty',0,'p_empty','Mparser.py',36),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instruction_opt_1','Mparser.py',41),
  ('instructions_opt -> empty','instructions_opt',1,'p_instruction_opt_2','Mparser.py',45),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',50),
  ('instructions -> instruction','instructions',1,'p_instructions','Mparser.py',51),
  ('instruction -> assignment','instruction',1,'p_instruction','Mparser.py',57),
  ('instruction -> conditional_statement','instruction',1,'p_instruction','Mparser.py',58),
  ('instruction -> print_statement','instruction',1,'p_instruction','Mparser.py',59),
  ('instruction -> jump_statement','instruction',1,'p_instruction','Mparser.py',60),
  ('instruction -> return_statement','instruction',1,'p_instruction','Mparser.py',61),
  ('instruction -> while_loop','instruction',1,'p_instruction','Mparser.py',62),
  ('instruction -> for_loop','instruction',1,'p_instruction','Mparser.py',63),
  ('instruction -> instruction_block','instruction',1,'p_instruction','Mparser.py',64),
  ('instruction_block -> { instructions }','instruction_block',3,'p_instruction_block','Mparser.py',70),
  ('assignment -> assign_id = expression ;','assignment',4,'p_assignment','Mparser.py',76),
  ('assignment -> assign_id MUL_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',77),
  ('assignment -> assign_id DIV_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',78),
  ('assignment -> assign_id PLUS_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',79),
  ('assignment -> assign_id SUB_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',80),
  ('assign_id -> ID','assign_id',1,'p_assign_id','Mparser.py',86),
  ('assign_id -> ID vector','assign_id',2,'p_assign_id','Mparser.py',87),
  ('expression -> expression_binop','expression',1,'p_expression','Mparser.py',92),
  ('expression -> expression_relop','expression',1,'p_expression','Mparser.py',93),
  ('expression -> expression_unary','expression',1,'p_expression','Mparser.py',94),
  ('expression -> matrix_funcs','expression',1,'p_expression','Mparser.py',95),
  ('expression -> constant','expression',1,'p_expression','Mparser.py',96),
  ('expression -> ID','expression',1,'p_expression','Mparser.py',97),
  ('expression -> matrix','expression',1,'p_expression','Mparser.py',98),
  ('expression -> ( expression )','expression',3,'p_expression','Mparser.py',99),
  ('expression_binop -> expression + expression','expression_binop',3,'p_expression_binop','Mparser.py',104),
  ('expression_binop -> expression - expression','expression_binop',3,'p_expression_binop','Mparser.py',105),
  ('expression_binop -> expression * expression','expression_binop',3,'p_expression_binop','Mparser.py',106),
  ('expression_binop -> expression / expression','expression_binop',3,'p_expression_binop','Mparser.py',107),
  ('expression_binop -> expression MATRIX_PLUS expression','expression_binop',3,'p_expression_binop','Mparser.py',108),
  ('expression_binop -> expression MATRIX_SUB expression','expression_binop',3,'p_expression_binop','Mparser.py',109),
  ('expression_binop -> expression MATRIX_MUL expression','expression_binop',3,'p_expression_binop','Mparser.py',110),
  ('expression_binop -> expression MATRIX_DIV expression','expression_binop',3,'p_expression_binop','Mparser.py',111),
  ('expression_relop -> expression RELOP_EQ expression','expression_relop',3,'p_expression_relop','Mparser.py',116),
  ('expression_relop -> expression RELOP_GT expression','expression_relop',3,'p_expression_relop','Mparser.py',117),
  ('expression_relop -> expression RELOP_LT expression','expression_relop',3,'p_expression_relop','Mparser.py',118),
  ('expression_relop -> expression RELOP_GE expression','expression_relop',3,'p_expression_relop','Mparser.py',119),
  ('expression_relop -> expression RELOP_LE expression','expression_relop',3,'p_expression_relop','Mparser.py',120),
  ('expression_relop -> expression RELOP_NE expression','expression_relop',3,'p_expression_relop','Mparser.py',121),
  ('expression_unary -> - expression','expression_unary',2,'p_expression_unary','Mparser.py',126),
  ("expression_unary -> expression '",'expression_unary',2,'p_expression_unary','Mparser.py',127),
  ('matrix_funcs -> ZEROS ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',133),
  ('matrix_funcs -> ONES ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',134),
  ('matrix_funcs -> EYE ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',135),
  ('constant -> DT_STRING','constant',1,'p_constant','Mparser.py',142),
  ('constant -> number','constant',1,'p_constant','Mparser.py',143),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix','Mparser.py',149),
  ('vectors -> vector','vectors',1,'p_vectors','Mparser.py',155),
  ('vectors -> vectors , vector','vectors',3,'p_vectors','Mparser.py',156),
  ('vector -> [ numbers ]','vector',3,'p_vector','Mparser.py',162),
  ('numbers -> numbers , number','numbers',3,'p_numbers','Mparser.py',168),
  ('numbers -> number','numbers',1,'p_numbers','Mparser.py',169),
  ('numbers -> empty','numbers',1,'p_numbers','Mparser.py',170),
  ('number -> DT_INTEGER','number',1,'p_number','Mparser.py',176),
  ('number -> DT_FLOAT','number',1,'p_number','Mparser.py',177),
  ('conditional_statement -> IF ( expression ) instruction','conditional_statement',5,'p_conditional_statement','Mparser.py',183),
  ('conditional_statement -> IF ( expression ) instruction ELSE instruction','conditional_statement',7,'p_conditional_statement','Mparser.py',184),
  ('jump_statement -> BREAK ;','jump_statement',2,'p_jump_statement','Mparser.py',190),
  ('jump_statement -> CONTINUE ;','jump_statement',2,'p_jump_statement','Mparser.py',191),
  ('return_statement -> RETURN ;','return_statement',2,'p_return_statement','Mparser.py',197),
  ('return_statement -> RETURN expression ;','return_statement',3,'p_return_statement','Mparser.py',198),
  ('print_statement -> PRINT expression_list ;','print_statement',3,'p_print_statement','Mparser.py',204),
  ('expression_list -> expression_list , expression','expression_list',3,'p_expression_list','Mparser.py',210),
  ('expression_list -> expression','expression_list',1,'p_expression_list','Mparser.py',211),
  ('while_loop -> WHILE ( expression ) instruction','while_loop',5,'p_while_loop','Mparser.py',217),
  ('for_loop -> FOR ID = range_value : range_value instruction','for_loop',7,'p_for_loop','Mparser.py',223),
  ('range_value -> DT_INTEGER','range_value',1,'p_range_value','Mparser.py',229),
  ('range_value -> ID','range_value',1,'p_range_value','Mparser.py',230),
]
