j=print
i=sorted
h=tuple
Y=next
X=enumerate
S=range
K=max
H=abs
import time as Z
from itertools import count
from collections import namedtuple as T
x='sunfish 2026'
J={'P':100,'N':280,'B':320,'R':479,'Q':929,'K':60000}
D={'P':(0,0,0,0,0,0,0,0,78,83,86,73,102,82,85,90,7,29,21,44,40,31,44,7,-17,16,-2,15,14,0,15,-13,-26,3,10,9,6,1,0,-23,-22,9,5,-11,-10,-2,3,-19,-31,8,-7,-37,-36,-14,3,-31,0,0,0,0,0,0,0,0),'N':(-66,-53,-75,-75,-10,-55,-58,-70,-3,-6,100,-36,4,62,-4,-14,10,67,1,74,73,27,62,-2,24,24,45,37,33,41,25,17,-1,5,31,21,22,35,2,0,-18,10,13,22,18,15,11,-14,-23,-15,2,0,2,0,-23,-20,-74,-23,-26,-24,-19,-35,-22,-69),'B':(-59,-78,-82,-76,-23,-107,-37,-50,-11,20,35,-42,-39,31,2,-22,-9,39,-32,41,52,-10,28,-14,25,17,20,34,26,25,15,10,13,10,17,23,17,16,0,7,14,25,24,15,8,25,20,15,19,20,11,6,7,6,20,16,-7,2,-15,-12,-14,-15,-10,-10),'R':(35,29,33,4,37,33,56,50,55,29,56,67,55,62,34,60,19,35,28,33,45,27,25,15,0,5,16,13,18,-4,-9,-6,-28,-35,-16,-21,-13,-29,-46,-30,-42,-28,-42,-25,-25,-35,-26,-46,-53,-38,-31,-26,-29,-43,-44,-53,-30,-24,-18,5,-2,-18,-31,-32),'Q':(6,1,-8,-104,69,24,88,26,14,32,60,-10,20,76,57,24,-2,43,32,60,72,63,43,2,1,-16,22,17,25,20,-13,-6,-14,-15,-2,-5,-1,-10,-20,-22,-30,-6,-13,-11,-16,-11,-16,-27,-36,-18,0,-19,-15,-15,-21,-38,-39,-30,-31,-13,-31,-36,-34,-42),'K':(4,54,47,-99,-99,60,83,-62,-32,10,55,56,56,55,10,3,-62,12,-57,44,-67,28,37,-31,-55,50,11,-4,-19,13,0,-49,-55,-43,-52,-28,-51,-47,-8,-50,-47,-42,-43,-79,-64,-32,-29,-32,-4,3,-14,-50,-57,-18,13,4,17,30,-3,-14,6,-1,40,18)}
for(L,k)in D.items():l=lambda row:(0,)+h(A+J[L]for A in row)+(0,);D[L]=sum((l(k[A*8:A*8+8])for A in S(8)),());D[L]=(0,)*20+D[L]+(0,)*20
m,n=D['K'],h(J['K']+70-10*(H(2*(A//10)-11)+H(2*(A%10)-9))for A in S(120))
I,M,N,O=91,98,21,28
y='         \n         \n rnbqkbnr\n pppppppp\n ........\n ........\n ........\n ........\n PPPPPPPP\n RNBQKBNR\n         \n         \n'
A,B,E,C=-10,1,10,-1
o={'P':(A,A+A,A+C,A+B),'N':(A+A+B,B+A+B,B+E+B,E+E+B,E+E+C,C+E+C,C+A+C,A+A+C),'B':(A+B,E+B,E+C,A+C),'R':(A,B,E,C),'Q':(A,B,E,C,A+B,E+B,E+C,A+C),'K':(A,B,E,C,A+B,E+B,E+C,A+C)}
P=J['K']-13*J['Q']
G=J['K']+10*J['Q']
a=36
p=180
q=70
U=15
r=-200
z=200
b=10**6
Q=T('Move','i j prom')
class V(T('Position','board score wc bc ep kp')):
	def gen_moves(E):
		for(F,J)in X(E.board):
			if J not in'PNBRQK':continue
			for G in o[J]:
				for D in count(F+G,G):
					K=E.board[D]
					if K in' \nPNBRQK':break
					if J=='P':
						if G in(A,A+A)and K!='.':break
						if G==A+A and(F<I+A or E.board[F+A]!='.'):break
						if G in(A+C,A+B)and K=='.'and D!=E.ep and H(D-E.kp)>1:break
						if N<=D<=O:yield from(Q(F,D,A)for A in'NBRQ');break
					yield Q(F,D,'')
					if J in'PNK'or K in'pnbrqk':break
					if F==I and E.board[D+B]=='K'and E.wc[0]:yield Q(D+B,D+C,'')
					if F==M and E.board[D+C]=='K'and E.wc[1]:yield Q(D+C,D+B,'')
	def rotate(A,nullmove=False):B=nullmove;return V(A.board[::-1].swapcase(),-A.score,A.bc,A.wc,119-A.ep if A.ep and not B else 0,119-A.kp if A.kp and not B else 0)
	def move(F,move):
		D,C,R=move;G=lambda board,i,p:board[:i]+p+board[i+1:];P,T,B,J,K,Q,L=F.board[D],F.board[C],F.board,F.wc,F.bc,0,0;S=F.score+F.value(move);B=G(B,C,B[D]);B=G(B,D,'.');J=J[0]and D!=I,J[1]and D!=M;K=K[0]and C!=O,K[1]and C!=N
		if P=='K':
			J=False,False
			if H(C-D)==2:L=(D+C)//2;B=G(B,I if C<D else M,'.');B=G(B,L,'R')
		if P=='P':
			if N<=C<=O:B=G(B,C,R)
			if C-D==2*A:Q=D+A
			if C==F.ep:B=G(B,C+E,'.')
		return V(B,S,J,K,Q,L).rotate()
	def value(F,move):
		C,A,K=move;G,J=F.board[C],F.board[A];B=D[G][A]-D[G][C]
		if J in'pnbrqk':B+=D[J.upper()][119-A]
		if H(A-F.kp)<2:B+=D['K'][119-A]
		if G=='K'and H(C-A)==2:B+=D['R'][(C+A)//2];B-=D['R'][I if A<C else M]
		if G=='P':
			if N<=A<=O:B+=D[K][A]-D['P'][A]
			if A==F.ep:B+=D['P'][119-(A+E)]
		return B
	def king_capture(A):return Y((B for B in A.gen_moves()if A.board[B.j]=='k'or H(B.j-A.kp)<2),None)
class c(Exception):0
W=T('Entry','lower upper')
class s:
	def __init__(A):A.tp_score,A.tp_move,A.history={},{},set();A.nodes,A.deadline,A.soft=0,1<<63,1<<63
	def bound(C,pos,gamma,depth,root=False):
		N=root;D=gamma;B=depth;A=pos;C.nodes+=1
		if C.nodes%2048==0 and Z.time()>C.deadline:raise c
		B=K(B,0)
		if A.score<=-P:return-G
		if not N:
			I=C.tp_score.get((A,B),W(-G,G))
			if I.lower>=D:return I.lower
			if I.upper<D:return I.upper
			if B>0 and A in C.history:return 0
		O=C.tp_move.get(A);R=lambda v:G if B>4 or v>=P else A.score+v+K(B-1,0)*p
		def X():
			if 2<B<6 and T:yield(None,None)
			if B==0:yield(None,None)
			if O and((C:=A.value(O))>=a or B)and R(C)>=D:yield(C,O)
			yield from i(((E,C)for C in A.gen_moves()if(E:=A.value(C))>=a or B),reverse=True)
		S=H(A.score)<750 and any(B in A.board for B in'RBNQ');T=not N and S;V=A.score+r;d=S and B>=6 and-C.bound(A.rotate(nullmove=True),1-V,B-7)>=V;E,M=-G,False
		for(Q,J)in X():
			if J is None and B==0:F=A.score
			elif J is None:
				if(L:=A.score+U)>=D:
					F=min(L,-C.bound(A.rotate(nullmove=True),1-D,B-4))
					if F>=D and(e:=A.king_capture()):J,F,M=e,G,True
				else:F=L
			elif Q>=P:F,M=G,True
			else:
				if(L:=R(Q))<D:E=K(E,L);break
				f=B-1-(T and B>=7 and Q<q)-int(d);F=min(L,-C.bound(A.move(J),1-D,f));M|=F>-G
			E=K(E,F)
			if E>=D:
				if J is not None and B:
					C.tp_move[A]=J
					if len(C.tp_move)>b:del C.tp_move[Y(A for A in C.tp_move if A!=C.root)]
				break
		if B and not M and all(A.move(B).king_capture()for B in A.gen_moves()):g=K(1-G,-P-B*U);E=g if A.rotate(nullmove=True).king_capture()else 0
		if not N:C.tp_score[A,B]=W(E,I.upper)if E>=D else W(I.lower,E)
		if len(C.tp_score)>b:del C.tp_score[Y(iter(C.tp_score))]
		return E
	def search(A,history):
		I=history;A.nodes,A.history,A.tp_score=0,set(I),{};E=A.root=I[-1];D['K']=m if'Q'in E.board and'q'in E.board else n;B=0
		for J in S(1,1000):
			F,H=1-G,G
			while F<H-U:
				C=A.bound(E,B,J,root=True)
				if C>=B:F=C
				if C<B:H=C
				yield(J,B,C,A.tp_move.get(E));B=(F+H+1)//2
			if Z.time()>A.soft:return
def d(i):return chr((i-I)%10+ord('a'))+str(1-(i-I)//10)
def t(board,wc=(True,True),bc=(True,True),ep=0,kp=0):A=board;B=sum(D[A][B]if A.isupper()else-D[A.upper()][119-B]for(B,A)in X(A)if A.isalpha());return V(A,B,wc,bc,ep,kp)
import os,sys,json as e,urllib.request as f
u=os.environ['MAKEFUN_ENV_URL']
def g(p,b):A=f.Request(u+p,data=e.dumps(b).encode(),headers={'content-type':'application/json'});return e.load(f.urlopen(A))
def v(fen):
	E=fen.split()[0].split('/');B=['.']*120
	for A in S(120):
		if A%10==9:B[A]='\n'
		elif A%10==0 or A<20 or A>=100:B[A]=' '
	for(F,G)in X(E):
		C=0
		for D in G:
			if D.isdigit():C+=int(D)
			else:B[21+10*F+C]=D;C+=1
	return''.join(B)
def w(fen):
	C=v(fen);F=fen.split()[1]=='b'
	if F:C=C[::-1].swapcase()
	G=t(C);B=s();B.node_cap=45000;A=None
	try:
		for(I,J,K,H)in B.search([G]):
			A=H
			if B.nodes>=B.node_cap:break
	except c:0
	if A is None:return
	D,E=A.i,A.j
	if F:D,E=119-D,119-E
	return d(D)+d(E)+A.prom.lower()
while 1:
	F=g('/game',{})
	if F['status']=='done':break
	while F['status']=='your_move':
		R=w(F['fen'])
		if R is None or R not in F['legal_moves']:R=i(F['legal_moves'])[0]
		F=g('/move',{'game':F['game'],'move':R})
	j(f"game {F['game']}: {F['outcome']} by {F['reason']}",file=sys.stderr)
j(f"done: {F.get('wins')} won, {F.get('draws')} drawn, {F.get('losses')} lost",file=sys.stderr)