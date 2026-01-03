---
layout: post
title:  "제1회 GSHS x SASA 프로그래밍 경시대회 Open Contest 참가 후기"
slug:   GSHSxSASA
date:   2026-01-03 10:50:00 +0900
categories: [Baekjoon, Open Contest]
tags: [PS]
---

## 서론
복슬님이 팀연습을 같이 돌자 제안하셔서 lntanz([<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl), [<span style="color: #ff8c00">**mythofys**</span>](https://codeforces.com/profile/mythofys), [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)) 팀으로 참여하였습니다.

제가 역대급 비틱으로 찍은 물레이팅라서 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl) 원맨쇼 버스타기가 되었습니다.

부산대에서 만나서 저녁을 먹고 셋을 돌기로 약속되었는데, 저희 집이 부산대에서 지하철을 타고 한 시간 반 거리라 3시에 집에서 출발하고 11시 반에 도착하는 일정이 되어버렸습니다.

[<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 늦잠을 자는 바람에 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)하고 둘이 저녁을 먹었습니다. 제육 + 백반 집이었는데, [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)가 밥을 사셔서 맛있게 멌었습니다. 감사합니다!

그러고는 최근 들어 제가 느낀 스피드 포스가 중요한 이유에 대한 설명을 막 늘어놓고 PS 관련 얘기를 하다가 대회 시작 30분 전에 세팅을 시작했습니다. 제가 말도 많고 목소리도 큰 편이라 불쾌하게 여길만한데, 내색하지 않고 잘 받아줘서 고마울 따름입니다.

노트북과 키보드, 충전기를 대충 세팅하고 전략을 세우니 5분 정도 남아서 새 계정을 만들어서 대회에 참여하기는 늦었다고 판단하고 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)님의 lntany계정을 사용하기로 하였습니다. 또, ICPC 연습이 주 목적이었기 때문에, 인터넷 사용이나 기존 코드 참고도 하지 않았고, 3인 1컴퓨터 대회로 머신을 번갈아가면서 집으며 참여하였습니다.

## 대회

![스코어보드 이미지](/assets/images/posts/GSHSxSASA/GSHSxSASA1.png)
A가 젤 어려울거라고 생각하고 A를 보는 사람이 문제 개수를 작게 집자라고 판단했는데, 둘 다 틀려서 결과적으로는 좋은 판단이 되었습니다.
[<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)이 ABC를, [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 DEFG를, 제가 HIJK를 집기로 하였습니다.

문제를 다 읽고 나서도 다들 풀이를 내지 못했고, 5분쯤 지난 시점에 스코어보드를 보니 A, C에 제출이 있길래 제가 C를 집었습니다.

대충 정리해보니 1 N-1 2 N-2 ... 순서로 인접한 gcd가 되게 배정하는 것이 답인 것으로 보였는데, 짜다보니 스코어보드에 빨간 줄이 그이길래 그 방법이 맞는지 다시 점검할 필요가 있었습니다.

[<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)가 A 풀이를 냈다길래 머신을 넘기고 식정리를 열심히 했습니다.

[<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)가 갑자기 __int128__을 어떻게 쓰는지 물었습니다. "그거 python 쓰면 안돼요?"를 시전하고 저는 C를 계속 봤고, 노트북 세팅을 대충해서 __int__128이 로컬에 컴파일이 안 된 덕분에 제출하면서 컴파일 에러가 나는지도 체크해야 했습니다. 그러다가 C 풀이가 나와서 머신을 넘겨달라고 하고, C를 짰는데 WA를 받았습니다.

[<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)에게 A를 짜라고 머신을 다시 넘기고 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 DEFG가 어려워 풀이가 나오지 않는다고 하여 C를 같이 봐달라고 했습니다.

아무리 봐도 증명이 틀릴리가 없었고, [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 assert를 짜서 검증하고 제출하라고 해서 다시 머신을 집고 검증을 assert를 돌려 통과하는지를 검증하고 냈습니다.

assert를 안 돌렸으면 아마 거진 4~5번은 더 틀렸을 것 같습니다.

그러고는 제가 슼보에서 그나마 젤 많이 풀린 K를 집었습니다. 딱봐도 자료구조를 적절히 잘 쓰는 문제 같았는데, 멀티셋 + 유니온 파인드로 관리하는 풀이가 빠르게 보여 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)에게 설명해주고 짜줘를 시전했습니다.

머신을 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 집고, [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)의 코드를 눈 디버깅하면서 문제를 읽어보는 와중 답 검증 과정이 long long 범위를 벗어나지 않는걸 발견하고 설명해줬습니다. 금방 고칠 수 있을 것 같다고 하여 머신을 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)이 집고 long long으로 고쳐서 냈고, 다행히 맞을 수 있었습니다.

다들 머신을 잡거나 풀이 구체화를 하는 사이 저는 H를 읽었고, 대충 N2^L개의 상태를 관리하면 되는 문제인걸 눈치채 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)에게 K를 짜고 H를 보면 짤 수 있을거니까 짜달라고 큐에 H를 추가했습니다.

제외하고는 슼보상으로는 F, G가 제일 풀만해보였고, 손으로 써봐도 모르겠어서 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 K짜는 걸 구경하다가 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)이 낸 F찍기 풀이 반례가 존재하는지 손으로 열심히 써봤습니다.

딱봐도 F가 대충 맞는 풀이 같아서 H를 짜다가 막히면 교대하기로 하였는데, H가 그냥 구현 문제인데다가 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 거의 다 짠 것 같아 H를 제출하고 F를 짜기로 하였습니다. H를 짰으나 WA가 나왔고, 머신을 교대하여 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)이 F를 짰습니다.

그 사이 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 H를 눈디버깅해서 틀린 곳을 찾았고, F도 WA를 받아 다시 교대했습니다. 다행히 틀린 곳을 고치니 맞았고, F도 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)이 문제를 다시 읽어보니 3대신 0을 출력하여 문제 조건에 위배되는 것을 확인했고, 해당 부분을 고쳐 내니 맞았습니다.

제가 스코어보드를 훑으니 스코어보드 아래쪽의 몇 팀도 B를 푼 것을 발견하고 B를 보았습니다. M제한이 매우 작기 때문에 그냥 A, B를 번갈아가며 bfs를 수행하되, A부터 시작하는 방법과 B부터 시작하는 방법 중 최소가 되는 방법으로 수행하면 될 것이라는 풀이를 냈고, 정당해보였습니다. bfs를 그냥 짜면 N^3으로 시간초과가 날 것 같은데, 어떻게 해결할지 몰라 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)에게 설명해주니 짤 수 있겠다고 하더니 200줄짜리 코드를 짜러 갔습니다.

그동안 [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)과 저는 나머지 문제 중 하나 이상의 풀이를 내보려고 하였으나 만만한 문제는 남아있지 않았고, 30분에서 1시간 가량 고민했으나 결론이 나오지 않았습니다.

그 사이 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 코드를 다 짜고 예제가 나온다길래 풀이 스케치 중 나왔던 데이터를 넣어 돌리고 맞으면 내보라고 하였고, 이가 답이 올바로 나오지 않아 디버깅을 거친 후 맞았습니다.

30분 밖에 남지 않아서 한 문제 이상만 풀면 성공이라는 마인드로 찍는 풀이라고 있으면 좋으니 짤 풀이가 있으면 풀이가 있는 사람이 짜기로 하였습니다. [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 몇 분 고민하더니 G 풀이를 찾은 것 같다면서 짜왔고 AC를 받았습니다. 레드는 다르긴 한가봅니다.

15분 정도 남았길래 풀이를 찾아도 못 짤 것 같아 저와 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)은 자리 정리를 시작했고, [<span style="color: #0000ff">**6729skl**</span>](https://codeforces.com/profile/Parkkkkkcw)은 I가 재미있어 보인다며 I를 쭉 집다가 대회가 종료되었습니다.

다른 모든 팀의 프리즈 이후 제출이 맞아도 순위가 3등인 것이 확정되었기 때문에 스코어보드가 풀리기 전부터 순위를 아는 상태로 구경하였습니다.

## 돌아볼 점
3시간 대회여서 확실히 시간이 짧다는 것이 느껴졌습니다. [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 문제 풀이를 내는데 힘 쓸 시간이 없었던 것 같은데, 제가 키보드를 쓰는 것보다 익숙한 사람이 쓰는게 빠르다고 키보드를 핵심 전략에게 토스한게 잘못된 판단이었나 봅니다. 이변이 없다면 UCPC를 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)과 나갈 예정이라 합을 맞추는게 상당히 중요한데, 웰노운 골드 ~ 플하위급 문제를 10 ~ 15분 정도 보면 풀이를 낼 수 있는 저와 30분 정도의 시간이 있으면 플 중 ~ 상위를 풀어낼 수 있는 괴물 같은 능력을 지닌 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)의 조합이 상당히 잘 맞는 것 같아 다행입니다.

특히, H와 K를 토스하지 말고, 제가 그냥 풀이를 내자 마자 집고 풀었다면 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 구현만 하다가 끝나 문제 풀이를 낼 시간이 부족하게 대회가 끝나지는 않았을 것 같은데 그게 아쉽습니다.

B번이 비교적 쉬운 문제인데 스코어보드를 보고 확인해서 핵심 관찰을 해서 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)에게 넘겨 준 점이나, 스코어보드를 따라 적당히 쉬운 골드 ~ 플 하위급 문제들을 빠르게 풀어낸 점은 성공적었습니다. C번 assert 검증을 하고 내라고 했던 [<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)의 판단도 상당히 좋았습니다. 아마 ICPC 본선을 겪고 최대한 검증하고 제출하려고 하는 것 같은데, 결과적으로 ICPC 아시아 챔피언십도 진출하고 발전할 수 있는 계기도 된 것 같아 좋게 작용한 것 같습니다.

## 여담
[<span style="color: #ff0000">**kolorvxl**</span>](https://codeforces.com/profile/kolorvxl)이 내년 연세대로 가는게 확정 된 것 같은데, 내년 연세대 팀이 우승 후보 중 하나로 꼽힐 것 같습니다. 이번 대회에서도 아무것도 안 했는데 버스를 탄 것 같아 상당히 좋았습니다.

검수진, 출제진 난이도를 대충 보니 셋이 5시간이면 나았을 것 같다는 생각은 듭니다. 물론 5시간 셋이라면 지하철 막차가 문제로 제가 참여하지는 못했겠지만요.

## 풀이
* **A** : 자기장에 관한 지문은 훼이크고 그냥 경로와 점이 주어지면 해당 경로 위에서 점과 가장 가까운 점을 찾는 문제입니다. 경로가 무조건 x좌표축이나 y좌표축에 평행하기 때문에 경로 선분의 시작점, 끝점, x좌표나 y좌표가 주어지는 점의 좌표와 같아지는 순간 3가지 경우만 잘 체크해주면 됩니다.
* **B** : ABAB..., BABA... 순서로 bfs하기 두 가지 경우만 고려해주면 최악의 경우에도 O(N)번만 bfs를 수행하여 풀 수 있습니다. 이미 방문한 칸을 방문하지 않게 잘 처리해주면 O(N)번의 bfs동안 최대 O(N^2)개의 칸만 방문하게 할 수 있습니다.
* **C** : 1 * 1, (n-1) * 1, (n-1) * 2, (n-2) * 2, ...으로 구성해주면 인접한 gcd가 각각 (1, n-1, 2, n-2, ... )이 되게 할 수 있습니다. 인접한 수의 gcd가 1이기 때문에 무조건 정확히 저 gcd값을 가진다는 것을 쉽게 증명할 수 있습니다. 제한이 살짝 타이트하여 잘못하면 a_i가 10^8을 넘을 수 있다는 것에 유의하여야 합니다.
* **F** : 1 0 2 1 0 2 ...로 배치하되, N을 3으로 나눈 나머지가 1, 2, 0일 때 각각 수를 어떻게 더 붙이는게 최악으로 만들 수 있는지를 고민한 다음 이게 최악일 것이라고 믿고 제출했습니다.
* **G** : 행, 열들 중 가장 최솟값이 최대인 행, 열들부터 순차적으로 연산해주면 그게 최대한 수를 줄이는 방법입니다.
* **H** : N * 2^L개의 상태 전부에 대해 머신 실행 중 중복되는 상태에 도착하면 머신이 종료되지 않고, 그 전에 종료된다면 멈춥니다.
* **K** : 각 좌표의 절댓값이 최종적으로 무엇이 되는지만 알면 충분합니다. map에 |x| + |y|를 기준으로 저장한 다음, 파라메트릭 서치를 합시다. 해당 하는 원소를 1 감소시켰을 때, 이미 맵에 존재하는 원소라면 두 원소는 앞으로 계속 함께 감소할 것이고, 같은 값을 가지므로 유니온 파인드를 이용해서 묶어줍시다. 최종적으로 유니온 파인드로 묶은 자료구조의 루트들의 값만으로 이루어진 map이 남고, 유니온 파인드의 루트 찾기 연산을 이용해서 각 좌표의 최종 절댓값의 합을 알 수 있습니다. 이를 안다면 좌표 절댓값이 그렇게 되게 구성하는 것은 쉬운 문제입니다. 초기에 |x| + |y|가 같은 값들을 유니온 파인드로 묶어야 한다는 것에 유의하여야 합니다.

긴 글 읽어주셔셔 감사합니다!