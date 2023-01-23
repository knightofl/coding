// html 이 돔트리에 구성되고 화면이 보이기 직전
// $(document).ready(function(){});
$(document).ready(()=>{
    //alert('dom');
    //form 태그의 submit 이벤트를 인터셉트
    //$('css 셀렉터') 형식으로 요소를 찾는다 => 현재 문서상의 모든 form 요소
    $('form').on('submit', (evt)=>{
        evt.preventDefault(); // 이벤트 무효화
        
        // ajax 통신수행
        console.log('ajax');
        $.post({
            url:'/search', // 서버 url
            data:$('form').serialize(), // 전달데이터 keyword=xxx&name=xxxx....
            dataType:'json', // 응답타입
            success:(data)=>{
                console.log('응답성공', data);
                // 검색어
                const word = $('input[name=keyword]').val();
                // 검색어 초기화
                $('#result b').empty();
                // 검색어 세팅
                $('#result b').append($('input[name=keyword]').val());
                // 검색창 초기화
                $('input[name=keyword]').val('');
                // 검색어 초기화
                $('#result ul').empty();
                // 주유소 이름과 가격 표시             
                $.each(data, (index, oil)=>{
                    console.log(oil.name, oil.gas)
                    var html = `<li>${oil.name} : 휘발유 ${oil.gas} 원</li>`;
                    $('#result ul').append(html.replace(word, `<b>${word}</b>`))
                    // 링크를 생성하여 클릭이벤트로 서브 페이지 이동
                    // 아이디가 result 인 요소의 자식/후손들 중에 ul
                    // ul 의 직계 자식들중 li
                    // 의사결정 셀렉터 ':'last (막내)
                    $('#result ul>li:last').on('click', ()=>{
                        if (confirm(`${oil.name}로 이동하시겠습니까?`))

                            document.location.href='/info/'+oil.id;
                    });

                });
            }, // 성공응답
            error:(err)=>{
                console.log('응답실패', err);
            } // 실패응답
        });

        // 이벤트 종료
        return false;
    });





});
