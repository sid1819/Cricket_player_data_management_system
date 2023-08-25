from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib.auth.models import User,auth
from home.models import *
from django.contrib import messages
 
 

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")
  

def contact(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       desc=request.POST.get('desc')

       
       contact=Contact(name=name,email=email,phone=phone,desc=desc, date=datetime.today())
       contact.save()
    return render(request,'contact.html')



def players(request):
    allPosts=Players.objects.all()
    print(type(allPosts))
    params={'allPosts': allPosts}
    print(allPosts)
    return render(request,'players.html',params)

def matches(request):
    allPosts=Match.objects.all()
    params={'allPosts':allPosts}
    return render (request,'matches.html',params)


def t20_ranking(request):
    #  return HttpResponse("this is t20 pages page")
     return render(request, 't20_ranking.html')

def oneday_ranking(request):
    #  return HttpResponse("this is t20 pages page")
     return render(request, 'oneday_ranking.html')

def test_ranking(request):
    #  return HttpResponse("this is t20 pages page")
     return render(request, 'test_ranking.html')

def ipl_ranking(request):
    #  return HttpResponse("this is t20 pages page")
     return render(request, 'ipl_ranking.html')





def t20_ranking_batsman1(request):
    # allPosts=Players.objects.all()
    params={'allPosts':Players.objects.all().order_by('-t20_run')[:9]}
    # print(allPosts)
    return render(request,'t20_batsman.html',params)
    # return render (request,'t20_batsman.html')

def t20_ranking_bowler1(request):
    # allPosts=t20_ranking_bowler.objects.all()
    params={'allPosts':Players.objects.all().order_by('-t20_wicket')[:9]}
    # params={'allPosts':allPosts}
    # print(allPosts)
    return render(request,'t20_bowler.html',params)


def oneday_ranking_batsman2(request):
    # allPosts=oneday_ranking_batsman.objects.all()
    # params={'allPosts':allPosts}
    params={'allPosts':Players.objects.all().order_by('-odi_run')[:9]}
    # print(allPosts)
    return render(request,'oneday_batsman.html',params)

def oneday_ranking_bowler2(request):
    # allPosts=oneday_ranking_bowler.objects.all()
    # params={'allPosts':allPosts}
    params={'allPosts':Players.objects.all().order_by('-odi_wicket')[:9]}
    # print(allPosts)
    return render(request,'oneday_bowler.html',params)


def test_ranking_batsman3(request):
   params={'allPosts':Players.objects.all().order_by('-test_run')[:9]}
   return render(request,'test_batsman.html',params)

def test_ranking_bowler3(request):
    params={'allPosts':Players.objects.all().order_by('-test_wicket')[:9]}
    return render(request,'test_bowler.html',params)

def ipl_ranking_batsman4(request):
   params={'allPosts':Players.objects.all().order_by('-ipl_run')[:9]}
   return render(request,'ipl_batsman.html',params)

def ipl_ranking_bowler4(request):
    params={'allPosts':Players.objects.all().order_by('-ipl_wicket')[:9]}
    return render(request,'ipl_bowler.html',params)



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            context={
                'p':Players.objects.all()
            }
            return render(request,'admin.html',context)
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def match(request):
    if request.method == "POST":     
        Match_Type=request.POST['Match_Type']
        date=request.POST['date']
        Team_A=request.POST['Team_A']
        Team_B=request.POST['Team_B']
        Toss_W_T=request.POST['Toss_W_T']
        Match_W_T=request.POST['Match_W_T']

        Player1_id=request.POST['Player1_id']
        Player_1_name=Players.objects.get(id=Player1_id).Name
        Player1_run=request.POST['Player1_run']
        Player1_b_p=request.POST['Player1_b_p']
        Player1_b_d=request.POST['Player1_b_d']         
        Player1_wicket=request.POST['Player1_wicket']
        p1=[Player1_id,Player1_run,Player1_b_p,Player1_b_d,Player1_wicket]

        Player2_id=request.POST['Player2_id']
        Player_2_name=Players.objects.get(id=Player2_id).Name
        Player2_run=request.POST['Player2_run']
        Player2_b_p=request.POST['Player2_b_p']
        Player2_b_d=request.POST['Player2_b_d']
        Player2_wicket=request.POST['Player2_wicket']
        p2=[Player2_id,Player2_run,Player2_b_p,Player2_b_d,Player2_wicket]


        Player3_id=request.POST['Player3_id']
        Player_3_name=Players.objects.get(id=Player3_id).Name
        Player3_run=request.POST['Player3_run']
        Player3_b_p=request.POST['Player3_b_p']
        Player3_b_d=request.POST['Player3_b_d']
        Player3_wicket=request.POST['Player3_wicket']
        p3=[Player3_id,Player3_run,Player3_b_p,Player3_b_d,Player3_wicket]

        Player4_id=request.POST['Player4_id']
        Player_4_name=Players.objects.get(id=Player4_id).Name
        Player4_run=request.POST['Player4_run']
        Player4_b_p=request.POST['Player4_b_p']
        Player4_b_d=request.POST['Player4_b_d']
        Player4_wicket=request.POST['Player4_wicket']
        p4=[Player4_id,Player4_run,Player4_b_p,Player4_b_d,Player4_wicket]

        Player5_id=request.POST['Player5_id']
        Player_5_name=Players.objects.get(id=Player5_id).Name
        Player5_run=request.POST['Player5_run']
        Player5_b_p=request.POST['Player5_b_p']
        Player5_b_d=request.POST['Player5_b_d']
        Player5_wicket=request.POST['Player5_wicket']
        p5=[Player5_id,Player5_run,Player5_b_p,Player5_b_d,Player5_wicket]

        Player6_id=request.POST['Player6_id']
        Player_6_name=Players.objects.get(id=Player6_id).Name
        Player6_run=request.POST['Player6_run']
        Player6_b_p=request.POST['Player6_b_p']
        Player6_b_d=request.POST['Player6_b_d']
        Player6_wicket=request.POST['Player6_wicket']
        p6=[Player6_id,Player6_run,Player6_b_p,Player6_b_d,Player6_wicket]

        Player7_id=request.POST['Player7_id']
        Player_7_name=Players.objects.get(id=Player7_id).Name
        Player7_run=request.POST['Player7_run']
        Player7_b_p=request.POST['Player7_b_p']
        Player7_b_d=request.POST['Player7_b_d']
        Player7_wicket=request.POST['Player7_wicket']
        p7=[Player7_id,Player7_run,Player7_b_p,Player7_b_d,Player7_wicket]

        Player8_id=request.POST['Player8_id']
        Player_8_name=Players.objects.get(id=Player8_id).Name
        Player8_run=request.POST['Player8_run']
        Player8_b_p=request.POST['Player8_b_p']
        Player8_b_d=request.POST['Player8_b_d']
        Player8_wicket=request.POST['Player8_wicket']
        p8=[Player8_id,Player8_run,Player8_b_p,Player8_b_d,Player8_wicket]

        Player9_id=request.POST['Player9_id']
        Player_9_name=Players.objects.get(id=Player9_id).Name
        Player9_run=request.POST['Player9_run']
        Player9_b_p=request.POST['Player9_b_p']
        Player9_b_d=request.POST['Player9_b_d']
        Player9_wicket=request.POST['Player9_wicket']
        p9=[Player9_id,Player9_run,Player9_b_p,Player9_b_d,Player9_wicket]

        Player10_id=request.POST['Player10_id']
        Player_10_name=Players.objects.get(id=Player10_id).Name
        Player10_run=request.POST['Player10_run']
        Player10_b_p=request.POST['Player10_b_p']
        Player10_b_d=request.POST['Player10_b_d']
        Player10_wicket=request.POST['Player10_wicket']
        p10=[Player10_id,Player10_run,Player10_b_p,Player10_b_d,Player10_wicket]

        Player11_id=request.POST['Player11_id']
        Player_11_name=Players.objects.get(id=Player11_id).Name
        Player11_run=request.POST['Player11_run']
        Player11_b_p=request.POST['Player11_b_p']
        Player11_b_d=request.POST['Player11_b_d']
        Player11_wicket=request.POST['Player11_wicket']
        p11=[Player11_id,Player11_run,Player11_b_p,Player11_b_d,Player11_wicket]

        Player12_id=request.POST['Player12_id']
        Player_12_name=Players.objects.get(id=Player12_id).Name
        Player12_run=request.POST['Player12_run']
        Player12_b_p=request.POST['Player12_b_p']
        Player12_b_d=request.POST['Player12_b_d']
        Player12_wicket=request.POST['Player12_wicket']
        p12=[Player12_id,Player12_run,Player12_b_p,Player12_b_d,Player12_wicket]

        Player13_id=request.POST['Player13_id']
        Player_13_name=Players.objects.get(id=Player13_id).Name
        Player13_run=request.POST['Player13_run']
        Player13_b_p=request.POST['Player13_b_p']
        Player13_b_d=request.POST['Player13_b_d']
        Player13_wicket=request.POST['Player13_wicket']
        p13=[Player13_id,Player13_run,Player13_b_p,Player13_b_d,Player13_wicket]

        Player14_id=request.POST['Player14_id']
        Player_14_name=Players.objects.get(id=Player14_id).Name
        Player14_run=request.POST['Player14_run']
        Player14_b_p=request.POST['Player14_b_p']
        Player14_b_d=request.POST['Player14_b_d']
        Player14_wicket=request.POST['Player14_wicket']
        p14=[Player14_id,Player14_run,Player14_b_p,Player14_b_d,Player14_wicket]

        Player15_id=request.POST['Player15_id']
        Player_15_name=Players.objects.get(id=Player15_id).Name
        Player15_run=request.POST['Player15_run']
        Player15_b_p=request.POST['Player15_b_p']
        Player15_b_d=request.POST['Player15_b_d']
        Player15_wicket=request.POST['Player15_wicket']
        p15=[Player15_id,Player15_run,Player15_b_p,Player15_b_d,Player15_wicket]

        Player16_id=request.POST['Player16_id']
        Player_16_name=Players.objects.get(id=Player16_id).Name
        Player16_run=request.POST['Player16_run']
        Player16_b_p=request.POST['Player16_b_p']
        Player16_b_d=request.POST['Player16_b_d']
        Player16_wicket=request.POST['Player16_wicket']
        p16=[Player16_id,Player16_run,Player16_b_p,Player16_b_d,Player16_wicket]

        Player17_id=request.POST['Player17_id']
        Player_17_name=Players.objects.get(id=Player17_id).Name
        Player17_run=request.POST['Player17_run']
        Player17_b_p=request.POST['Player17_b_p']
        Player17_b_d=request.POST['Player17_b_d']
        Player17_wicket=request.POST['Player17_wicket']
        p17=[Player17_id,Player17_run,Player17_b_p,Player17_b_d,Player17_wicket]

        Player18_id=request.POST['Player18_id']
        Player_18_name=Players.objects.get(id=Player18_id).Name
        Player18_run=request.POST['Player18_run']
        Player18_b_p=request.POST['Player18_b_p']
        Player18_b_d=request.POST['Player18_b_d']
        Player18_wicket=request.POST['Player18_wicket']
        p18=[Player18_id,Player18_run,Player18_b_p,Player18_b_d,Player18_wicket]

        Player19_id=request.POST['Player19_id']
        Player_19_name=Players.objects.get(id=Player19_id).Name
        Player19_run=request.POST['Player19_run']
        Player19_b_p=request.POST['Player19_b_p']
        Player19_b_d=request.POST['Player19_b_d']
        Player19_wicket=request.POST['Player19_wicket']
        p19=[Player19_id,Player19_run,Player19_b_p,Player19_b_d,Player19_wicket]

        Player20_id=request.POST['Player20_id']
        Player_20_name=Players.objects.get(id=Player20_id).Name
        Player20_run=request.POST['Player20_run']
        Player20_b_p=request.POST['Player20_b_p']
        Player20_b_d=request.POST['Player20_b_d']
        Player20_wicket=request.POST['Player20_wicket']
        p20=[Player20_id,Player20_run,Player20_b_p,Player20_b_d,Player20_wicket]

        Player21_id=request.POST['Player21_id']
        Player_21_name=Players.objects.get(id=Player21_id).Name
        Player21_run=request.POST['Player21_run']
        Player21_b_p=request.POST['Player21_b_p']
        Player21_b_d=request.POST['Player21_b_d']
        Player21_wicket=request.POST['Player21_wicket']
        p21=[Player21_id,Player21_run,Player21_b_p,Player21_b_d,Player21_wicket]

        Player22_id=request.POST['Player22_id']
        Player_22_name=Players.objects.get(id=Player22_id).Name
        Player22_run=request.POST['Player22_run']
        Player22_b_p=request.POST['Player22_b_p']
        Player22_b_d=request.POST['Player22_b_d']
        Player22_wicket=request.POST['Player22_wicket']
        p22=[Player22_id,Player22_run,Player22_b_p,Player22_b_d,Player22_wicket]


        Match(Match_Type=Match_Type,date=date,Team_A=Team_A,Team_B=Team_B,Toss_W_T=Toss_W_T,Match_W_T=Match_W_T,Player1_id=Player1_id,Player_1_name=Player_1_name,Player1_run=Player1_run,Player1_b_p=Player1_b_p,Player1_b_d=Player1_b_d,Player1_wicket=Player1_wicket,Player2_id=Player2_id,Player_2_name=Player_2_name,Player2_run=Player2_run,Player2_b_p=Player2_b_p,Player2_b_d=Player2_b_d,Player2_wicket=Player2_wicket,Player3_id=Player3_id,Player_3_name=Player_3_name,Player3_run=Player3_run,Player3_b_p=Player3_b_p,Player3_b_d=Player3_b_d,Player3_wicket=Player3_wicket,Player4_id=Player4_id,Player_4_name=Player_4_name,Player4_run=Player4_run,Player4_b_p=Player4_b_p,Player4_b_d=Player4_b_d,Player4_wicket=Player4_wicket,Player5_id=Player5_id,Player_5_name=Player_5_name,Player5_run=Player5_run,Player5_b_p=Player5_b_p,Player5_b_d=Player5_b_d,Player5_wicket=Player5_wicket,Player6_id=Player6_id,Player_6_name=Player_6_name,Player6_run=Player6_run,Player6_b_p=Player6_b_p,Player6_b_d=Player6_b_d,Player6_wicket=Player6_wicket,Player7_id=Player7_id,Player_7_name=Player_7_name,Player7_run=Player7_run,Player7_b_p=Player7_b_p,Player7_b_d=Player7_b_d,Player7_wicket=Player7_wicket,Player8_id=Player8_id,Player_8_name=Player_8_name,Player8_run=Player8_run,Player8_b_p=Player8_b_p,Player8_b_d=Player8_b_d,Player8_wicket=Player8_wicket,Player9_id=Player9_id,Player_9_name=Player_9_name,Player9_run=Player9_run,Player9_b_p=Player9_b_p,Player9_b_d=Player9_b_d,Player9_wicket=Player9_wicket,Player10_id=Player10_id,Player_10_name=Player_10_name,Player10_run=Player10_run,Player10_b_p=Player10_b_p,Player10_b_d=Player10_b_d,Player10_wicket=Player10_wicket,Player11_id=Player11_id,Player_11_name=Player_11_name,Player11_run=Player11_run,Player11_b_p=Player11_b_p,Player11_b_d=Player11_b_d,Player11_wicket=Player11_wicket,Player12_id=Player12_id,Player_12_name=Player_12_name,Player12_run=Player12_run,Player12_b_p=Player12_b_p,Player12_b_d=Player12_b_d,Player12_wicket=Player12_wicket,Player13_id=Player13_id,Player_13_name=Player_13_name,Player13_run=Player13_run,Player13_b_p=Player13_b_p,Player13_b_d=Player13_b_d,Player13_wicket=Player13_wicket,Player14_id=Player14_id,Player_14_name=Player_14_name,Player14_run=Player14_run,Player14_b_p=Player14_b_p,Player14_b_d=Player14_b_d,Player14_wicket=Player14_wicket,Player15_id=Player15_id,Player_15_name=Player_15_name,Player15_run=Player15_run,Player15_b_p=Player15_b_p,Player15_b_d=Player15_b_d,Player15_wicket=Player15_wicket,Player16_id=Player16_id,Player_16_name=Player_16_name,Player16_run=Player16_run,Player16_b_p=Player16_b_p,Player16_b_d=Player16_b_d,Player16_wicket=Player16_wicket,Player17_id=Player17_id,Player_17_name=Player_17_name,Player17_run=Player17_run,Player17_b_p=Player17_b_p,Player17_b_d=Player17_b_d,Player17_wicket=Player17_wicket,Player18_id=Player18_id,Player_18_name=Player_18_name,Player18_run=Player18_run,Player18_b_p=Player18_b_p,Player18_b_d=Player18_b_d,Player18_wicket=Player18_wicket,Player19_id=Player19_id,Player_19_name=Player_19_name,Player19_run=Player19_run,Player19_b_p=Player19_b_p,Player19_b_d=Player19_b_d,Player19_wicket=Player19_wicket,Player20_id=Player20_id,Player_20_name=Player_20_name,Player20_run=Player20_run,Player20_b_p=Player20_b_p,Player20_b_d=Player20_b_d,Player20_wicket=Player20_wicket,Player21_id=Player21_id,Player_21_name=Player_21_name,Player21_run=Player21_run,Player21_b_p=Player21_b_p,Player21_b_d=Player21_b_d,Player21_wicket=Player21_wicket,Player22_id=Player22_id,Player_22_name=Player_22_name,Player22_run=Player22_run,Player22_b_p=Player22_b_p,Player22_b_d=Player22_b_d,Player22_wicket=Player22_wicket).save()


        p=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22]

        if Match_Type=='T20':
            for item in p:
                id=item[0]
                pm=Players.objects.get(id=id).t20_matches
                pr=Players.objects.get(id=id).t20_run
                pbp=Players.objects.get(id=id).t20_b_p
                pw=Players.objects.get(id=id).t20_wicket
                pbd=Players.objects.get(id=id).t20_b_d
                pd=Players.objects.get(id=id).t20_dcentury
                pc=Players.objects.get(id=id).t20_century
                pf=Players.objects.get(id=id).t20_fifty
                Players.objects.filter(id=id).update(t20_matches = (pm+1))
                Players.objects.filter(id=id).update(t20_run = (int(pr)+int(item[1])))
                Players.objects.filter(id=id).update(t20_b_p = (int(pbp)+int(item[2])))
                Players.objects.filter(id=id).update(t20_wicket = (int(pw)+int(item[3])))
                Players.objects.filter(id=id).update(t20_b_d = (int(pbd)+int(item[4])))
                Players.objects.filter(id=id).update(t20_average = ((int(pr)+int(item[1]))/(pm+1)))
                if (int(pbp)+int(item[2]))>=1:
                    Players.objects.filter(id=id).update(t20_strike_rate = 100*((int(pr)+int(item[1]))/(int(pbp)+int(item[2]))))
                if (int(item[1]))>=200:
                    Players.objects.filter(id=id).update(t20_dcentury = (pd+1))
                elif ((int(item[1]))>=100) and ((int(item[1]))<200):
                    Players.objects.filter(id=id).update(t20_century = (pc+1))
                elif ((int(item[1]))>=50) and ((int(item[1]))<100):
                    Players.objects.filter(id=id).update(t20_fifty = (pf+1))
        elif Match_Type=='Test':
            for item in p:
                id=item[0]
                pm=Players.objects.get(id=id).test_matches
                pr=Players.objects.get(id=id).test_run
                pbp=Players.objects.get(id=id).test_b_p
                pw=Players.objects.get(id=id).test_wicket
                pbd=Players.objects.get(id=id).test_b_d
                pd=Players.objects.get(id=id).test_dcentury
                pc=Players.objects.get(id=id).test_century
                pf=Players.objects.get(id=id).test_fifty
                Players.objects.filter(id=id).update(test_matches = (pm+1))
                Players.objects.filter(id=id).update(test_run = (int(pr)+int(item[1])))
                Players.objects.filter(id=id).update(test_b_p = (int(pbp)+int(item[2])))
                Players.objects.filter(id=id).update(test_wicket = (int(pw)+int(item[3])))
                Players.objects.filter(id=id).update(test_b_d = (int(pbd)+int(item[4])))
                Players.objects.filter(id=id).update(test_average = ((int(pr)+int(item[1]))/(pm+1)))
                if (int(pbp)+int(item[2]))>1:
                    Players.objects.filter(id=id).update(test_strike_rate = 100*((int(pr)+int(item[1]))/(int(pbp)+int(item[2]))))
                if (int(item[1]))>=200:
                    Players.objects.filter(id=id).update(test_dcentury = (pd+1))
                elif ((int(item[1]))>=100) and ((int(item[1]))<200):
                    Players.objects.filter(id=id).update(test_century = (pc+1))
                elif ((int(item[1]))>=50) and ((int(item[1]))<100):
                    Players.objects.filter(id=id).update(test_fifty = (pf+1))
        elif Match_Type=='One Day':
            for item in p:
                id=item[0]
                pm=Players.objects.get(id=id).odi_matches
                pr=Players.objects.get(id=id).odi_run
                pbp=Players.objects.get(id=id).odi_b_p
                pw=Players.objects.get(id=id).odi_wicket
                pbd=Players.objects.get(id=id).odi_b_d
                pd=Players.objects.get(id=id).odi_dcentury
                pc=Players.objects.get(id=id).odi_century
                pf=Players.objects.get(id=id).odi_fifty
                Players.objects.filter(id=id).update(odi_matches = (pm+1))
                Players.objects.filter(id=id).update(odi_run = (int(pr)+int(item[1])))
                Players.objects.filter(id=id).update(odi_b_p = (int(pbp)+int(item[2])))
                Players.objects.filter(id=id).update(odi_wicket = (int(pw)+int(item[3])))
                Players.objects.filter(id=id).update(odi_b_d = (int(pbd)+int(item[4])))
                Players.objects.filter(id=id).update(odi_average = ((int(pr)+int(item[1]))/(pm+1)))
                if (int(pbp)+int(item[2]))>1:
                    Players.objects.filter(id=id).update(odi_strike_rate = 100*((int(pr)+int(item[1]))/(int(pbp)+int(item[2]))))
                if (int(item[1]))>=200:
                    Players.objects.filter(id=id).update(odi_dcentury = (pd+1))
                elif ((int(item[1]))>=100) and ((int(item[1]))<200):
                    Players.objects.filter(id=id).update(odi_century = (pc+1))
                elif ((int(item[1]))>=50) and ((int(item[1]))<100):
                    Players.objects.filter(id=id).update(odi_fifty = (pf+1))
        else:
             for item in p:
                id=item[0]
                pm=Players.objects.get(id=id).ipl_matches
                pr=Players.objects.get(id=id).ipl_run
                pbp=Players.objects.get(id=id).ipl_b_p
                pw=Players.objects.get(id=id).ipl_wicket
                pbd=Players.objects.get(id=id).ipl_b_d
                pd=Players.objects.get(id=id).ipl_dcentury
                pc=Players.objects.get(id=id).ipl_century
                pf=Players.objects.get(id=id).ipl_fifty
                Players.objects.filter(id=id).update(ipl_matches = (pm+1))
                Players.objects.filter(id=id).update(ipl_run =(int(pr)+int(item[1])))
                Players.objects.filter(id=id).update(ipl_b_p =(int(pbp)+int(item[2])))
                Players.objects.filter(id=id).update(ipl_wicket =(int(pw)+int(item[3])))
                Players.objects.filter(id=id).update(ipl_b_d =(int(pbd)+int(item[4])))
                Players.objects.filter(id=id).update(ipl_average =((int(pr)+int(item[1]))/(pm+1)))
                if (int(pbp)+int(item[2]))>1:
                    Players.objects.filter(id=id).update(ipl_strike_rate = 100*((int(pr)+int(item[1]))/(int(pbp)+int(item[2]))))
                if (int(item[1]))>=200:
                    Players.objects.filter(id=id).update(ipl_dcentury = (pd+1))
                elif ((int(item[1]))>=100) and ((int(item[1]))<200):
                    Players.objects.filter(id=id).update(ipl_century = (pc+1))
                elif ((int(item[1]))>=50) and ((int(item[1]))<100):
                    Players.objects.filter(id=id).update(ipl_fifty = (pf+1))
        
    return redirect("home")

