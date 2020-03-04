#Verificação de tipo

"1 - Eb = Eb 'ou' Tb"
{
  Nterm Eb; Eb.tp = Bool; Eb.nome = geraTemp();
  if ( Eb.tp != Bool || Tb.tp != Bool ){
    throw erro (" 'ou' com operandos não booleanos", ou);
  }
}
                               
"2 - Eb = tb"
{
  Nterm Eb = Tb
}

"3 - Tb = Tb 'e' Fb"
{
  Nterm Tb; Tb.tp = Bool; Tb.nome = geraTemp();
  if ( Tb.tp != Bool || Fb.tp != Bool){
  throw erro (" 'e' com operandos não booleanos", e);
  }
}
                               
"4 - Tb = Fb"
{
  Nterm Tb = fb
}

"5 - Fb = 'not' Fb1"           
{
  Nterm Fb; Fb.tp = Bool; Fb.nome = geraTemp();
  if ( Fb1.tp != Bool ){
    throw erro (" 'not' com operando não booleano", not);
  }
}
                               
"6 - Fb = Er"                  
{
  Nterm Fb = Er
}

"7 - Er = Tr 'relg' Tr1"       
{
  Nterm Er; Er.tp = Bool; Er.nome = geraTemp();
  if ( Tr.tp == Bool || Tr1.tp == Bool ){
  throw erro (" 'relg' com operandos booleanos", relg);
  }
}
                               
"8 - Er = Tr" 
{
  Nterm Er = Tr
}

"9 - Tr = Ea 'relig' Ea1"      
{
  Nterm Tr; Tr.tp = Bool; Tr.nome = geraTemp();
  if ( Ea.tp != Ea1.tp ){
  throw erro (" 'relig' com operandos incompátiveis", relig);
  }
}
                               
"10 - Tr = Ea"                  
{
  Nterm Tr = Ea
}

"11 - Ea = Ea1 'opa' Ta"        
{
  Nterm Ea;Ea.nome = geraTemp();
  if ( Ea1.tp == Bool || Ta.tp == Bool ){
       throw erro (" 'opa' com operandos booleanos", opa);
     }
  else if ( Ea1.tp == Float || Ta.tp == Float){
       Ea.tp = Float;
     }
  else{
       Ea.tp = Int;
     }
 }
                                                     
"12 - Ea = Ta"
{
  Nterm Ea = Ta
}

"13 - Ta = Ta1 'opm' Pa"        
{
  Nterm Ta; Ta.nome = geraTemp();
  if ( Ta1.tp == Bool || Pa.tp == Bool ){
       throw erro (" 'opm' com operandos booleanos", opm);
     }
  else if ( Ta1.tp == Float || Pa.tp == Float){
       Ta.tp = Float;
     }
  else{
       Ta.tp = Int;
       } 
}                         
                               
"14 - Ta = Pa"                 
{
  Nterm Ta = Pa
}

"15 - Pa = Fa ** Pa"            
{
  Nterm Pa, Pa.nome = geraTemp(), Pa.tp = Undef;
  if ( Fa.tp == Pa1.tp){
     Pa.tp = Fa.tp;
  }
  else if ( Pa1.tp == int ) {
     Pa.tp = Fa.tp;
   }
  else {
       throw erro( " '**' com operandos incompatíveis ", exp );
     }
  if ( Pa.tp != int || Pa.tp != float ){
    throw erro ( " '**' Com operandos incompatíveis ", exp );
  }
}
                              
"16 - Pa = Fa"                  
{
  Nterm Pa = Fa
}

"17 - Fa = '(' Eb ')'"          
{
  Nterm Fa = Eb
}

"18 - Fa = 'id'"                
{
  Nterm Fa;
  if ((Fa.tp = verTs(id.lex)) == Undef){
    throw erro(" 'id' não definido ", id);
    fa.nome = id.lex;
  }
}
                          
"19 - Fa = 'cteI'"              
{
  Nterm Fa; Fa.tp = Int;
  Fa.nome = adTctei(cteI.lex);
}
                          
"20 - Fa = 'cteF'"               
{
  Nterm Fa; Fa.tp = Float;
  Fa.nome = adTcteF(cteF.lex);
}
                          
"21 - Fa = 'verd'"               
{
  Nterm Fa; Fa.tp = Bool; 
  Fa.nome = _Verd;
}

"22 - Fa = 'falso'"              
{
  Nterm Fa; Fa.tp = Bool; 
  Fa.nome = _Falso;
}





