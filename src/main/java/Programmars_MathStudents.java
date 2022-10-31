/*
    2차원 배열: 찍는 패턴을  각각의 배열에 저장
    배열당 pointer하나
    correct[]: 학생들의 맞힌 개수
    highest: 가장 높은 점수
    arraylist: 가장 높은 점수를 받은 학생

    for loop: 학생 수
        for loop: 질문 개수
            if answer[j] == patter[student(바깥 쪽 loop)][pointer]
                 correct[i]++;

    가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
        if pattern[student] > highest
            arraylist에 replace
    if
 */



public class Programmars_MathStudents {


