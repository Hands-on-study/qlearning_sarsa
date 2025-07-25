## Play

python3.8~3.9

그 이후로는 되는지 test 안해봄. 


```bash
pip install -r requirement.txt
```


## Environment

<p style="font-family:Arial; font-size:16px;">
5 x 5 grid world 
</p>

agent는 빨간색 rectangle이다.  
initialize state에서 agent는 좌측 최상단에 위치한다.

한번의 action 마다 agent는 상하좌우로 1칸씩만 이동 가능하다.  
terminal state는 초록색 triangle, 파란색 circle이다.  
agent가 초록색 triangle을 만나면 reward -100 을, 파란색 원을 만나면 reward 100을 얻으며, 그외엔 reward 0을 얻는다. 



<p align="center">
  <img src="img/gridworld.png" width="350">
</p>


## Q-learning
<p align="center">
  <img src="img/Qlearning_pseudocode.png" width="1200">
</p>

- $Q(S, A)$ update에 $Q(S', a)$가 사용되었으므로 bootstrapping
- 1-step transition인 $(S,A,R,S')$ 을 바탕으로 update가 진행 (TD 방식)
- Target policy는 Q에 대한 $\text{greedy}$, behavior policy는 Q에 대한 $\epsilon -\text{greedy}$ (Off policy)
- $Q^*$ 를 target으로 하여 학습이 진행되기 때문에 Bellman optimality equation 사용
- 직접 Optimal Q-function을 학습하기 때문에 성능 우수


## SARSA

<p align="center">
  <img src="img/SARSA_pseudocode.png" width="1200">
</p>

- $Q(S, A)$ update에 $Q(S', A')$가 사용되었으므로 bootstrapping
- 1-step transition인 $(S,A,R,S',A')$ 을 바탕으로 update가 진행(TD 방식)
- Target policy와 behavior policy가 Q에 대한 $\epsilon -\text{greedy}$ policy로 동일(On policy)
- $Q^\pi$를 target으로 하여 학습이 진행되기 때문에 Bellman expectation equation 사용




## Q1.
q_learning 폴더의 main_q를 debugging 해보면서 "?" 를 정답으로 채우시오.  
주의! state를 input으로 줄거라면 반드시 str(state)로 해야하며, environmnet.py에는 빈칸없습니다.



## Q2.
sarsa 폴더의 main_s를 debugging 해보면서 "?" 를 정답으로 채우시오.  
주의! state를 input으로 줄거라면 반드시 str(state)로 해야하며, environmnet.py에는 빈칸없습니다.



## Q3.
SARSA과 Q-learning을 돌렸을 때, 보기엔 SARSA가 굉장히 멍청한거 같다. 이에 대한 해결법을 서술하시오.  
(Hint: environment와 관련이 있다. Cliff Walking 에서는 왜 SARSA가 좋게 나왔을까?)

answer: sarsa는 패널티를 고려해서  the cliff를 고려하기 때문에 safe path를 선택하는 것 
q-learning는 패널티를  고려하지 않기 때문에 the cliff를 고려하지 않아 optimal path로 가는 것 

<p align="center">
  <img src="img/cliff_walking.png" width="1200">
</p>


## Q4.
같은 ε-greedy 정책을 사용하더라도 Q-learning과 SARSA가 서로 다른 학습 결과를 보일 수 있는 이유는 무엇인가?
다음 보기 중 올바른 것을 모두 고르시오.


a. Q-learning은 실제로 선택된 행동을 사용하여 Q를 업데이트한다.

b. SARSA는 ε-greedy 정책에 따라 선택된 다음 행동을 학습에 사용한다.

c. Q-learning은 항상 최적의 행동만을 사용하여 Q를 업데이트한다.  

d. SARSA는 환경 모델을 알고 있어야 작동한다.

answer: b,c 

## Q5.
SARSA와 Q-learning 2가지 방식 모두 epsilon-greedy를 사용한다.  
그러나 SARSA는 그 값을 작게, Q-learning을 크게 사용한다.  
그 이유를 서술하시오.

answer: sarsa는 target policy를 작게 q-learning은 target policy를 크게 
아마도  sarsa는  $Q ^{\pi}$ , q-learning은 Q* 이기 때문에 

## git push
```bash
git checkout -b your-branch-name
# 예: git checkout -b SH

git add .
git commit -m "message"
# 예: git commit -m "Add solution by SH"

git push origin your-branch-name
# 예: git push origin SH
```
