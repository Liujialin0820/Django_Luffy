#   D j a n g o _ L u f f y  
  
  
  
 #   ,{ N�z 
  
 # #   �OV�S 
  
 ` ` ` p y t h o n  
 p i p   i n s t a l l   d j a n g o    
 p i p   i n s t a l l   d j a n g o r e s t f r a m e w o r k    
 p i p   i n s t a l l   P y m y S Q L    
 p i p   i n s t a l l   P i l l o w    
 p i p   i n s t a l l   d j a n g o - r e d i s    
 ` ` `  
  
  
  
 # #   y��v/T�R 
  
 ` ` ` s h e l l  
 d j a n g o - a d m i n   s t a r t p r o j e c t   l u f f y a p i   .  
 ` ` `  
  
  
  
 # #   �te�vU_ 
  
 ` ` `  
 l u f f y /  
     % % %  d o c s /                     #   y��v�vsQD��e�OX[�vU_ 
     % % %  l u f f y c i t y /           #   MR�zy��v�vU_ 
     % % %  l u f f y a p i /             #   T�zy��v�vU_ 
               % % %  l o g s /                     #   y��vЏL��e/  _�S�e�e�_�vU_ 
               % % %  m a n a g e . p y  
               % % %  l u f f y a p i /             #   y��v;N�^(u� _�S�e�v�Nx�OX[ 
               %        % % %  a p p s /             #    _�S��v�Nx�OX[�vU_��N!jWW[ P[�^(u] :N�vU_�OX[ 
               %        % % %  l i b s /             #   ,{	N�e{|�^�v�OX[�vU_[ ,{	N�e�~�N0!jWW]  
               %        % % %  s e t t i n g s /  
               %                  % % %  d e v . p y       #   y��v _�S�e�v,g0WM�n 
               %                  % % %  p r o d . p y     #   y��v
N�~�e�vЏL�M�n 
               %        % % %  u r l s . p y         #   ;`�1u 
               %        % % %  u t i l s /           #   Y*N!jWW[ P[�^(u] �vlQqQ�Qpe{|�^[ ��] _�S�v�~�N]  
               % % %  s c r i p t s /               #   �OX[y��vЏ%��e�v�,g�e�N 
 ` ` `  
  
 m a n a g e . p y   ��n  s e t t i n g s  
  
 ` ` ` p y t h o n  
         o s . e n v i r o n . s e t d e f a u l t ( ' D J A N G O _ S E T T I N G S _ M O D U L E ' ,   ' l u f f y a p i . s e t t i n g s . d e v ' )   # c�[0Rs e t t i n g s 
N 
 ` ` `  
  
  
  
 # #   �e�_M�n 
  
 ` ` ` p y t h o n  
 #   �e�_M�n 
 L O G G I N G   =   {  
         ' v e r s i o n ' :   1 ,  
         ' d i s a b l e _ e x i s t i n g _ l o g g e r s ' :   F a l s e ,  
         ' f o r m a t t e r s ' :   {  
                 ' v e r b o s e ' :   {  
                         ' f o r m a t ' :   ' % ( l e v e l n a m e ) s   % ( a s c t i m e ) s   % ( m o d u l e ) s   % ( l i n e n o ) d   % ( m e s s a g e ) s '  
                 } ,  
                 ' s i m p l e ' :   {  
                         ' f o r m a t ' :   ' % ( l e v e l n a m e ) s   % ( m o d u l e ) s   % ( l i n e n o ) d   % ( m e s s a g e ) s '  
                 } ,  
         } ,  
         ' f i l t e r s ' :   {  
                 ' r e q u i r e _ d e b u g _ t r u e ' :   {  
                         ' ( ) ' :   ' d j a n g o . u t i l s . l o g . R e q u i r e D e b u g T r u e ' ,  
                 } ,  
         } ,  
         ' h a n d l e r s ' :   {  
                 ' c o n s o l e ' :   {  
                         ' l e v e l ' :   ' D E B U G ' ,  
                         ' f i l t e r s ' :   [ ' r e q u i r e _ d e b u g _ t r u e ' ] ,  
                         ' c l a s s ' :   ' l o g g i n g . S t r e a m H a n d l e r ' ,  
                         ' f o r m a t t e r ' :   ' s i m p l e '  
                 } ,  
                 ' f i l e ' :   {  
                         ' l e v e l ' :   ' I N F O ' ,  
                         ' c l a s s ' :   ' l o g g i n g . h a n d l e r s . R o t a t i n g F i l e H a n d l e r ' ,  
                         #   �e�_MOn, �e�_�e�NT, �e�_�OX[�vU_�_{�Kb�RR�^ 
                         ' f i l e n a m e ' :   o s . p a t h . j o i n ( o s . p a t h . d i r n a m e ( B A S E _ D I R ) ,   " l o g s / l u f f y . l o g " ) ,  
                         #   �e�_�e�N�v g'Y<P, ُ̑b�N��n3 0 0 M  
                         ' m a x B y t e s ' :   3 0 0   *   1 0 2 4   *   1 0 2 4 ,  
                         #   �e�_�e�N�vpeϑ, ��n g'Y�e�_peϑ:N1 0  
                         ' b a c k u p C o u n t ' :   1 0 ,  
                         #   �e�_<h_: ��~<h_ 
                         ' f o r m a t t e r ' :   ' v e r b o s e '  
                 } ,  
         } ,  
         #   �e�_�[a� 
         ' l o g g e r s ' :   {  
                 ' d j a n g o ' :   {  
                         ' h a n d l e r s ' :   [ ' c o n s o l e ' ,   ' f i l e ' ] ,  
                         ' p r o p a g a t e ' :   T r u e ,   #   /f&T���e�_�Oo`�~�~�Q�l�~vQ�N�v�e�_Yt�|�~ 
                 } ,  
         }  
 }  
 ` ` `  
  
 