
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEnonassocRELOP_EQRELOP_NERELOP_GTRELOP_LTRELOP_GERELOP_LEleft+-leftMATRIX_PLUSMATRIX_SUBleft*/leftMATRIX_MULMATRIX_DIVrightUMINUSleft'BREAK CONTINUE DIV_ASSIGN DT_FLOAT DT_INTEGER DT_STRING ELSE EYE FOR ID IF MATRIX_DIV MATRIX_MUL MATRIX_PLUS MATRIX_SUB MUL_ASSIGN ONES PLUS_ASSIGN PRINT RELOP_EQ RELOP_GE RELOP_GT RELOP_LE RELOP_LT RELOP_NE RETURN SUB_ASSIGN WHILE ZEROSprogram : instructions_opt\n        empty : \n    instructions_opt : instructions instructions_opt : empty \n        instructions : instructions instruction\n    \n        instructions : instruction\n    \n        instruction : assignment\n                    | conditional_statement\n                    | print_statement\n                    | jump_statement\n                    | return_statement\n                    | while_loop\n                    | for_loop\n                    | instruction_block\n    \n        instruction_block : '{' instructions '}'\n    \n        assignment : assign_id '=' expression ';'\n                    | assign_id MUL_ASSIGN expression ';'\n                    | assign_id DIV_ASSIGN expression ';'\n                    | assign_id PLUS_ASSIGN expression ';'\n                    | assign_id SUB_ASSIGN expression ';'\n    \n        assign_id : ID\n                  | ID vector\n    expression : expression_binop\n                  | expression_relop\n                  | expression_unary\n                  | matrix_funcs\n                  | constant\n                  | matrix\n                  | vector\n    expression : ID\n    expression : '(' expression ')'\n    expression_binop : expression '+' expression\n                | expression '-' expression\n                | expression '*' expression\n                | expression '/' expression\n                | expression MATRIX_PLUS expression\n                | expression MATRIX_SUB expression\n                | expression MATRIX_MUL expression\n                | expression MATRIX_DIV expression\n    expression_relop : expression RELOP_EQ expression\n                | expression RELOP_GT expression\n                | expression RELOP_LT expression\n                | expression RELOP_GE expression\n                | expression RELOP_LE expression\n                | expression RELOP_NE expression\n    expression_unary : '-' expression %prec UMINUS\n                | expression '\\''\n    \n        matrix_funcs : ZEROS '(' expression_list ')'\n                    | ONES '(' expression_list ')'\n                    | EYE '(' expression_list ')'  \n\n    \n        constant : number\n    \n        constant : DT_STRING\n    \n        matrix : '[' vectors ']'\n\n     vectors : vector \n     vectors : vectors ',' vector\n    \n        vector : '[' numbers ']'\n                | '[' ']'\n    \n        numbers : numbers ',' number \n                | number\n    \n        number : DT_INTEGER \n    \n        number : DT_FLOAT\n    \n        conditional_statement : IF '(' expression ')' instruction %prec IFX\n                    | IF '(' expression ')' instruction ELSE instruction\n    \n        jump_statement : BREAK ';'\n                        | CONTINUE ';'\n    \n        return_statement : RETURN ';'\n                        | RETURN expression ';'\n    \n        print_statement : PRINT expression_list ';'\n    \n        expression_list : expression_list ',' expression\n    \n        expression_list : expression\n    \n        while_loop : WHILE '(' expression ')' instruction\n    \n        for_loop : FOR ID '=' range_value ':' range_value instruction\n    \n        range_value : DT_INTEGER                   \n    \n        range_value : ID                   \n    "
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,24,51,52,53,66,93,96,97,98,99,100,101,130,136,140,141,],[-2,0,-1,-3,-4,-6,-7,-8,-9,-10,-11,-12,-13,-14,-5,-64,-65,-66,-68,-67,-15,-16,-17,-18,-19,-20,-62,-71,-63,-72,]),'IF':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[15,15,-6,-7,-8,-9,-10,-11,-12,-13,-14,15,-5,-64,-65,-66,15,-68,-67,-15,-16,-17,-18,-19,-20,15,15,-74,-73,-62,-71,15,15,-63,-72,]),'PRINT':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[16,16,-6,-7,-8,-9,-10,-11,-12,-13,-14,16,-5,-64,-65,-66,16,-68,-67,-15,-16,-17,-18,-19,-20,16,16,-74,-73,-62,-71,16,16,-63,-72,]),'BREAK':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[17,17,-6,-7,-8,-9,-10,-11,-12,-13,-14,17,-5,-64,-65,-66,17,-68,-67,-15,-16,-17,-18,-19,-20,17,17,-74,-73,-62,-71,17,17,-63,-72,]),'CONTINUE':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[18,18,-6,-7,-8,-9,-10,-11,-12,-13,-14,18,-5,-64,-65,-66,18,-68,-67,-15,-16,-17,-18,-19,-20,18,18,-74,-73,-62,-71,18,18,-63,-72,]),'RETURN':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[19,19,-6,-7,-8,-9,-10,-11,-12,-13,-14,19,-5,-64,-65,-66,19,-68,-67,-15,-16,-17,-18,-19,-20,19,19,-74,-73,-62,-71,19,19,-63,-72,]),'WHILE':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[20,20,-6,-7,-8,-9,-10,-11,-12,-13,-14,20,-5,-64,-65,-66,20,-68,-67,-15,-16,-17,-18,-19,-20,20,20,-74,-73,-62,-71,20,20,-63,-72,]),'FOR':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[21,21,-6,-7,-8,-9,-10,-11,-12,-13,-14,21,-5,-64,-65,-66,21,-68,-67,-15,-16,-17,-18,-19,-20,21,21,-74,-73,-62,-71,21,21,-63,-72,]),'{':([0,3,5,6,7,8,9,10,11,12,13,23,24,51,52,53,59,66,93,96,97,98,99,100,101,102,126,127,129,130,136,138,139,140,141,],[23,23,-6,-7,-8,-9,-10,-11,-12,-13,-14,23,-5,-64,-65,-66,23,-68,-67,-15,-16,-17,-18,-19,-20,23,23,-74,-73,-62,-71,23,23,-63,-72,]),'ID':([0,3,5,6,7,8,9,10,11,12,13,16,19,21,23,24,25,26,27,28,29,30,41,42,51,52,53,55,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,93,95,96,97,98,99,100,101,102,126,127,129,130,136,137,138,139,140,141,],[22,22,-6,-7,-8,-9,-10,-11,-12,-13,-14,40,40,56,22,-5,40,40,40,40,40,40,40,40,-64,-65,-66,40,22,-68,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-67,127,-15,-16,-17,-18,-19,-20,22,22,-74,-73,-62,-71,127,22,22,-63,-72,]),'}':([5,6,7,8,9,10,11,12,13,24,51,52,53,59,66,93,96,97,98,99,100,101,130,136,140,141,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-5,-64,-65,-66,96,-68,-67,-15,-16,-17,-18,-19,-20,-62,-71,-63,-72,]),'ELSE':([6,7,8,9,10,11,12,13,51,52,53,66,93,96,97,98,99,100,101,130,136,140,141,],[-7,-8,-9,-10,-11,-12,-13,-14,-64,-65,-66,-68,-67,-15,-16,-17,-18,-19,-20,138,-71,-63,-72,]),'=':([14,22,56,57,89,124,],[25,-21,95,-22,-57,-56,]),'MUL_ASSIGN':([14,22,57,89,124,],[26,-21,-22,-57,-56,]),'DIV_ASSIGN':([14,22,57,89,124,],[27,-21,-22,-57,-56,]),'PLUS_ASSIGN':([14,22,57,89,124,],[28,-21,-22,-57,-56,]),'SUB_ASSIGN':([14,22,57,89,124,],[29,-21,-22,-57,-56,]),'(':([15,16,19,20,25,26,27,28,29,30,41,42,43,44,45,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[30,41,41,55,41,41,41,41,41,41,41,41,85,86,87,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'-':([16,19,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,46,47,49,50,54,55,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[42,42,42,42,42,42,42,42,69,-23,-24,-25,-26,-27,-28,-29,-30,42,42,-51,-52,-60,-61,69,42,69,69,69,69,69,69,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-47,69,-46,42,42,42,-57,69,69,-32,-33,-34,-35,-36,-37,-38,-39,69,69,69,69,69,69,-31,-53,-56,-48,-49,-50,]),'ZEROS':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ONES':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'EYE':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'DT_STRING':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'[':([16,19,22,25,26,27,28,29,30,41,42,48,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,123,],[48,48,58,48,48,48,48,48,48,48,48,58,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,58,]),'DT_INTEGER':([16,19,25,26,27,28,29,30,41,42,48,55,58,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,95,125,137,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,129,49,129,]),'DT_FLOAT':([16,19,25,26,27,28,29,30,41,42,48,55,58,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,125,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),';':([17,18,19,31,32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,82,84,89,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[51,52,53,66,-70,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,93,97,98,99,100,101,-47,-46,-57,-69,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-31,-53,-56,-48,-49,-50,]),',':([31,32,33,34,35,36,37,38,39,40,46,47,49,50,82,84,88,89,90,91,92,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,131,132,133,134,135,],[67,-70,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,-47,-46,123,-57,125,-54,-59,-69,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-31,67,67,67,-53,-56,-48,-49,-50,-55,-58,]),')':([32,33,34,35,36,37,38,39,40,46,47,49,50,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,131,132,133,],[-70,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,102,-47,118,-46,-57,126,-69,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-31,131,132,133,-53,-56,-48,-49,-50,]),'+':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[68,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,68,68,68,68,68,68,68,-47,68,-46,-57,68,68,-32,-33,-34,-35,-36,-37,-38,-39,68,68,68,68,68,68,-31,-53,-56,-48,-49,-50,]),'*':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[70,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,70,70,70,70,70,70,70,-47,70,-46,-57,70,70,70,70,-34,-35,70,70,-38,-39,70,70,70,70,70,70,-31,-53,-56,-48,-49,-50,]),'/':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[71,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,71,71,71,71,71,71,71,-47,71,-46,-57,71,71,71,71,-34,-35,71,71,-38,-39,71,71,71,71,71,71,-31,-53,-56,-48,-49,-50,]),'MATRIX_PLUS':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[72,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,72,72,72,72,72,72,72,-47,72,-46,-57,72,72,72,72,-34,-35,-36,-37,-38,-39,72,72,72,72,72,72,-31,-53,-56,-48,-49,-50,]),'MATRIX_SUB':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[73,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,73,73,73,73,73,73,73,-47,73,-46,-57,73,73,73,73,-34,-35,-36,-37,-38,-39,73,73,73,73,73,73,-31,-53,-56,-48,-49,-50,]),'MATRIX_MUL':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[74,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,74,74,74,74,74,74,74,-47,74,-46,-57,74,74,74,74,74,74,74,74,-38,-39,74,74,74,74,74,74,-31,-53,-56,-48,-49,-50,]),'MATRIX_DIV':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[75,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,75,75,75,75,75,75,75,-47,75,-46,-57,75,75,75,75,75,75,75,75,-38,-39,75,75,75,75,75,75,-31,-53,-56,-48,-49,-50,]),'RELOP_EQ':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[76,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,76,76,76,76,76,76,76,-47,76,-46,-57,76,76,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),'RELOP_GT':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[77,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,77,77,77,77,77,77,77,-47,77,-46,-57,77,77,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),'RELOP_LT':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[78,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,78,78,78,78,78,78,78,-47,78,-46,-57,78,78,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),'RELOP_GE':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[79,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,79,79,79,79,79,79,79,-47,79,-46,-57,79,79,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),'RELOP_LE':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[80,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,80,80,80,80,80,80,80,-47,80,-46,-57,80,80,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),'RELOP_NE':([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[81,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,81,81,81,81,81,81,81,-47,81,-46,-57,81,81,-32,-33,-34,-35,-36,-37,-38,-39,None,None,None,None,None,None,-31,-53,-56,-48,-49,-50,]),"'":([32,33,34,35,36,37,38,39,40,46,47,49,50,54,60,61,62,63,64,65,82,83,84,89,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,124,131,132,133,],[82,-23,-24,-25,-26,-27,-28,-29,-30,-51,-52,-60,-61,82,82,82,82,82,82,82,-47,82,82,-57,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-31,-53,-56,-48,-49,-50,]),']':([48,49,50,58,88,89,90,91,92,124,134,135,],[89,-60,-61,89,122,-57,124,-54,-59,-56,-55,-58,]),':':([127,128,129,],[-74,137,-73,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,23,],[3,59,]),'empty':([0,],[4,]),'instruction':([0,3,23,59,102,126,138,139,],[5,24,5,24,130,136,140,141,]),'assignment':([0,3,23,59,102,126,138,139,],[6,6,6,6,6,6,6,6,]),'conditional_statement':([0,3,23,59,102,126,138,139,],[7,7,7,7,7,7,7,7,]),'print_statement':([0,3,23,59,102,126,138,139,],[8,8,8,8,8,8,8,8,]),'jump_statement':([0,3,23,59,102,126,138,139,],[9,9,9,9,9,9,9,9,]),'return_statement':([0,3,23,59,102,126,138,139,],[10,10,10,10,10,10,10,10,]),'while_loop':([0,3,23,59,102,126,138,139,],[11,11,11,11,11,11,11,11,]),'for_loop':([0,3,23,59,102,126,138,139,],[12,12,12,12,12,12,12,12,]),'instruction_block':([0,3,23,59,102,126,138,139,],[13,13,13,13,13,13,13,13,]),'assign_id':([0,3,23,59,102,126,138,139,],[14,14,14,14,14,14,14,14,]),'expression_list':([16,85,86,87,],[31,119,120,121,]),'expression':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[32,54,60,61,62,63,64,65,83,84,94,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,32,32,32,]),'expression_binop':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'expression_relop':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'expression_unary':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'matrix_funcs':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'constant':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'matrix':([16,19,25,26,27,28,29,30,41,42,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'vector':([16,19,22,25,26,27,28,29,30,41,42,48,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,123,],[39,39,57,39,39,39,39,39,39,39,39,91,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,134,]),'number':([16,19,25,26,27,28,29,30,41,42,48,55,58,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,87,125,],[46,46,46,46,46,46,46,46,46,46,92,46,92,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,135,]),'vectors':([48,],[88,]),'numbers':([48,58,],[90,90,]),'range_value':([95,137,],[128,139,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',38),
  ('empty -> <empty>','empty',0,'p_empty','Mparser.py',44),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instruction_opt_1','Mparser.py',50),
  ('instructions_opt -> empty','instructions_opt',1,'p_instruction_opt_2','Mparser.py',55),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',61),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',70),
  ('instruction -> assignment','instruction',1,'p_instruction','Mparser.py',81),
  ('instruction -> conditional_statement','instruction',1,'p_instruction','Mparser.py',82),
  ('instruction -> print_statement','instruction',1,'p_instruction','Mparser.py',83),
  ('instruction -> jump_statement','instruction',1,'p_instruction','Mparser.py',84),
  ('instruction -> return_statement','instruction',1,'p_instruction','Mparser.py',85),
  ('instruction -> while_loop','instruction',1,'p_instruction','Mparser.py',86),
  ('instruction -> for_loop','instruction',1,'p_instruction','Mparser.py',87),
  ('instruction -> instruction_block','instruction',1,'p_instruction','Mparser.py',88),
  ('instruction_block -> { instructions }','instruction_block',3,'p_instruction_block','Mparser.py',96),
  ('assignment -> assign_id = expression ;','assignment',4,'p_assignment','Mparser.py',103),
  ('assignment -> assign_id MUL_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',104),
  ('assignment -> assign_id DIV_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',105),
  ('assignment -> assign_id PLUS_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',106),
  ('assignment -> assign_id SUB_ASSIGN expression ;','assignment',4,'p_assignment','Mparser.py',107),
  ('assign_id -> ID','assign_id',1,'p_assign_id','Mparser.py',116),
  ('assign_id -> ID vector','assign_id',2,'p_assign_id','Mparser.py',117),
  ('expression -> expression_binop','expression',1,'p_expression','Mparser.py',126),
  ('expression -> expression_relop','expression',1,'p_expression','Mparser.py',127),
  ('expression -> expression_unary','expression',1,'p_expression','Mparser.py',128),
  ('expression -> matrix_funcs','expression',1,'p_expression','Mparser.py',129),
  ('expression -> constant','expression',1,'p_expression','Mparser.py',130),
  ('expression -> matrix','expression',1,'p_expression','Mparser.py',131),
  ('expression -> vector','expression',1,'p_expression','Mparser.py',132),
  ('expression -> ID','expression',1,'p_expression_2','Mparser.py',138),
  ('expression -> ( expression )','expression',3,'p_expression_3','Mparser.py',145),
  ('expression_binop -> expression + expression','expression_binop',3,'p_expression_binop','Mparser.py',151),
  ('expression_binop -> expression - expression','expression_binop',3,'p_expression_binop','Mparser.py',152),
  ('expression_binop -> expression * expression','expression_binop',3,'p_expression_binop','Mparser.py',153),
  ('expression_binop -> expression / expression','expression_binop',3,'p_expression_binop','Mparser.py',154),
  ('expression_binop -> expression MATRIX_PLUS expression','expression_binop',3,'p_expression_binop','Mparser.py',155),
  ('expression_binop -> expression MATRIX_SUB expression','expression_binop',3,'p_expression_binop','Mparser.py',156),
  ('expression_binop -> expression MATRIX_MUL expression','expression_binop',3,'p_expression_binop','Mparser.py',157),
  ('expression_binop -> expression MATRIX_DIV expression','expression_binop',3,'p_expression_binop','Mparser.py',158),
  ('expression_relop -> expression RELOP_EQ expression','expression_relop',3,'p_expression_relop','Mparser.py',166),
  ('expression_relop -> expression RELOP_GT expression','expression_relop',3,'p_expression_relop','Mparser.py',167),
  ('expression_relop -> expression RELOP_LT expression','expression_relop',3,'p_expression_relop','Mparser.py',168),
  ('expression_relop -> expression RELOP_GE expression','expression_relop',3,'p_expression_relop','Mparser.py',169),
  ('expression_relop -> expression RELOP_LE expression','expression_relop',3,'p_expression_relop','Mparser.py',170),
  ('expression_relop -> expression RELOP_NE expression','expression_relop',3,'p_expression_relop','Mparser.py',171),
  ('expression_unary -> - expression','expression_unary',2,'p_expression_unary','Mparser.py',178),
  ("expression_unary -> expression '",'expression_unary',2,'p_expression_unary','Mparser.py',179),
  ('matrix_funcs -> ZEROS ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',192),
  ('matrix_funcs -> ONES ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',193),
  ('matrix_funcs -> EYE ( expression_list )','matrix_funcs',4,'p_matrix_funcs','Mparser.py',194),
  ('constant -> number','constant',1,'p_constant','Mparser.py',204),
  ('constant -> DT_STRING','constant',1,'p_constant_str','Mparser.py',211),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix','Mparser.py',219),
  ('vectors -> vector','vectors',1,'p_vectors','Mparser.py',227),
  ('vectors -> vectors , vector','vectors',3,'p_vectors_2','Mparser.py',234),
  ('vector -> [ numbers ]','vector',3,'p_vector','Mparser.py',243),
  ('vector -> [ ]','vector',2,'p_vector','Mparser.py',244),
  ('numbers -> numbers , number','numbers',3,'p_numbers','Mparser.py',257),
  ('numbers -> number','numbers',1,'p_numbers','Mparser.py',258),
  ('number -> DT_INTEGER','number',1,'p_number_int','Mparser.py',272),
  ('number -> DT_FLOAT','number',1,'p_number_float','Mparser.py',281),
  ('conditional_statement -> IF ( expression ) instruction','conditional_statement',5,'p_conditional_statement','Mparser.py',290),
  ('conditional_statement -> IF ( expression ) instruction ELSE instruction','conditional_statement',7,'p_conditional_statement','Mparser.py',291),
  ('jump_statement -> BREAK ;','jump_statement',2,'p_jump_statement','Mparser.py',302),
  ('jump_statement -> CONTINUE ;','jump_statement',2,'p_jump_statement','Mparser.py',303),
  ('return_statement -> RETURN ;','return_statement',2,'p_return_statement','Mparser.py',311),
  ('return_statement -> RETURN expression ;','return_statement',3,'p_return_statement','Mparser.py',312),
  ('print_statement -> PRINT expression_list ;','print_statement',3,'p_print_statement','Mparser.py',326),
  ('expression_list -> expression_list , expression','expression_list',3,'p_expression_list','Mparser.py',334),
  ('expression_list -> expression','expression_list',1,'p_expression_list_2','Mparser.py',342),
  ('while_loop -> WHILE ( expression ) instruction','while_loop',5,'p_while_loop','Mparser.py',349),
  ('for_loop -> FOR ID = range_value : range_value instruction','for_loop',7,'p_for_loop','Mparser.py',356),
  ('range_value -> DT_INTEGER','range_value',1,'p_range_value_int','Mparser.py',363),
  ('range_value -> ID','range_value',1,'p_range_value_id','Mparser.py',371),
]
