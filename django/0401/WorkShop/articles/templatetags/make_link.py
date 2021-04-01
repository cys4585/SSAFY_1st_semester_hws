from django import template


register = template.Library()

@register.filter
def make_link(article):
    # 본문 + ' '
        # 마지막에 공백 넣어주는 이유? hashtag는 공백 기준으로 만들기 때문에
        # 마지막 공백이 있어야 밑에서 정상적으로 링크를 만들고
        # 본문 내용을 그대로 유지할 수 있다.
    content = article.content + ' '
    # 각각의 해시태그들의 정보를 가져오기 위해서
    # article과 관계되어 있는 모든 hashtag 가져오기
    hashtags = article.hashtags.all()

    for hashtag in hashtags:
        # 본문을 변경 할거다.
        content = content.replace(
            # 원래 가지고 있던 hashtag + ' '
            # 여기에 공백이 들어가는 이유는?
            # 본문상에는 hashtag가 공백 기준으로 나눠져 있지만,
            # hashtag에는 공백이 없으므로, 바꿀때도 공백 추가해서 바꿀 것이다.
            # oldvalue
            hashtag.content + ' ',
            # newvalue (링크로)
            f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> '
        )
    # 원문 content
    '''
        test
        #hash_tag
    '''
    # 바꿔준 content
    '''
        test
        <a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a>
    '''
    return content