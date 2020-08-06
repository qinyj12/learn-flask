## I'm just learing flask deeply.
看到这里了：https://dormousehole.readthedocs.io/en/latest/patterns/viewdecorators.html
只做了一个登录模板，还没存储在g中
想把登录状态存储在session里，然后在装饰器里判断session里有没有登录状态（因为g不知道为什么拿不到）
现在要解决session的跨域问题，似乎要先解决secure connection的问题（https）