winCounter = 0
def optimizeTeam(my_team, opp_team):
    #print(len(my_team))
    #print(" ============================= /n /n /n ")
    #print(len(opp_team))
    for i in range(len(my_team)):
        for j in range(len(opp_team)):
            print(my_team[i], opp_team[j])

if __name__ == "__main__":
    #481
    #468 expected
    T = 10
    blades = "3 6 7 5 3 5 6 2 9 1"
    roudies = "2 7 0 9 3 6 0 6 2 6"
    blades = "28013 18171 19169 15795 6429 7405 31298 26402 5208 27108 26537 29003 4349 27599 7828 10696 5649 32310 31420 29307 24252 3371 7996 27682 10900 13437 26868 12075 25375 24366 24624 1737 14994 31527 28037 25159 10207 5419 22012 28829 25583 28938 17011 6721 19500 29207 22079 19775 20035 26587 6422 20364 16680 4875 14381 2967 20314 30392 25245 2850 22120 18886 17675 5200 24500 7327 26760 7423 5751 1832 30902 2135 24325 29429 13612 25251 29523 21945 4636 3936 10422 28672 19507 7572 17133 25632 29633 13922 30818 14700 13082 23002 2989 8108 21564 24086 7770 1738 18866 25730 8428 24270 16056 14715 1057 5132 29343 21020 3960 7068 25459 23636 241 9227 3036 5436 23060 15952 14402 22952 32308 4866 14132 9469 1525 30664 26891 29250 27660 30992 29386 13177 30534 11268 6217 21295 1484 23737 403 29778 7589 27818 28556 25667 26236 30054 9175 29484 28836 901 32758 9876 27993 32224 8115 31280 15433 3330 29375 8956 29267 5849 6554 2187 15758 8881 2482 26779 19085 14692 15567 22765 3809 5578 28590 6996 7392 14711 13292 30731 25765 14758 22823 4683 1624 22640 29023 27421 6576 15938 29858 1646 3765 26509 18408 26209 3019 6847 11068 20713 27884 31347 21276 5014 18485 2020 12579 14767 7076 10664 12261 26754 2080 2715 26139 22008 15801 25881 1280 3436 32050 3696 1530 30397 21180 22164 23421 21410 28165 4117 10540 10046 15217 21583 18242 15349 8871 22497 5425 15229 3664 25440 24457 3384 8475 17484 23834 28353 15365 19010 1885 31429 14807 9332 21008 4628 1008 13143 1569 23287 25668 8859 17357 19141 14501 24416 28681 28081 27458 16039 4385 24806 21613 26630 24223 13014 27041 22689 2158 7630 24003 4693 31039 20686 5800 19254 6188 15001 7128 12604 19867 2824 25233 5689 20326 24227 6927 6158 30777 18546 25355 6431 11835 11793 386 7428 7408 10755 4023 23938 18014 26696 13179 11193 12142 12594 20140 29086 11158 5748 18428 26540 2997 30332 20723 21207 13374 18947 19768 24258 24217 28642 16140 26673 2502 27431 23831 19393 24132 18280 13671 3287 2353 5975 438 26838 21170 16791 4331 10901 29589 4046 27108 21008 28213 13308 2931 25693 28318 14347 28070 30690 30194 2983 10316 20678 21772 9295 25268 8613 14946 25516 28856 17544 22320 14370 16634 20 24531 11174 110 11521 27506 21711 5913 20430 30436 24111 25112 31411 3790 6115 20195 3032 25868 18281 15315 7108 21843 10674 16866 12312 7444 23416 19379 1661 19107 7122 7634 3035 10136 7430 13372 21452 8822 22430 6434 9296 31626 5054 6378 27074 14614 7348 30583 9994 9903 21201 2730 13845 25572 3959 24104 27778 17952 3956 17502 30878 4562 22414 30915 2707 20170 18271 14173 7644 15334 20068 28039 30460 9711 30544 26609 10608 9662 15782 8680 14818 2467 24966 6616 12447 28167 11719 20239 12363 18767 25671 19651 25812 28420 17535 26199 24228 20017 24667 2266 11803 28429 13128 17873 "
    roudies = "21308 29658 12174 31542 21926 8461 13792 15552 6342 12463 11057 25189 16460 29955 8394 24606 14555 3689 17050 19178 14597 14466 32717 12053 20086 29333 8608 7098 19311 1842 17523 1927 10359 14101 26399 29376 11853 2892 1163 27270 31776 4765 27514 20826 15874 3618 18599 4317 10139 20790 5908 6361 1818 22677 27295 20357 1137 23742 18646 22277 24770 25500 1036 19505 18964 5478 19629 25239 5963 22724 27854 451 87 31283 25096 18366 9899 25258 18823 5332 497 8574 21086 1178 1276 19843 10781 30768 3838 372 6054 5572 31995 30612 14396 24919 28541 2198 4829 21188 6282 4538 30162 3326 9683 1594 21124 6809 6958 12260 2961 21388 12614 25352 26911 20533 3217 10644 10097 3485 24707 10622 21432 9982 21250 19042 27435 18562 13337 24173 28761 16206 24048 21113 27326 19135 20732 10617 1173 4851 24691 18200 15086 26764 771 19869 21504 12720 7107 4882 4032 10324 20330 29093 18099 19899 14783 30542 27392 14137 5968 14514 8137 6205 14183 19272 23227 11663 19002 10938 17380 28117 24418 3470 18373 9052 10382 27909 4009 21269 21625 17475 21557 5342 5657 19121 15935 16643 11290 11680 18916 5893 31882 3375 24532 16794 6358 16494 6385 23540 15861 9411 24601 23622 9443 31885 26175 1925 14161 8456 7361 21100 31899 2929 10741 21442 21242 31082 3077 11231 18683 12447 24062 1389 11055 9642 29475 4972 6692 2612 15495 12408 15509 1629 11483 847 25054 8542 3716 19598 10418 7533 32753 16827 32272 19170 2603 6536 2163 5783 1453 11606 21322 22420 16759 21497 20135 8172 8286 22971 30523 5346 8358 14755 14978 4688 466 31735 27451 7498 31931 24063 23067 27134 16864 9996 26306 30942 12797 20153 7406 3842 1247 22641 12783 3527 21110 2097 30299 28093 12844 21647 4098 24768 25717 14844 4132 24420 15015 21318 14818 9623 12557 23393 3315 25217 28470 31846 26776 8111 8851 4060 23250 9073 26434 13367 28626 21120 13092 23454 5553 21732 30517 14321 26721 533 27421 10251 31204 22625 14082 2628 27323 909 28577 6202 26274 14015 6301 12242 22906 23964 8470 11641 28807 26797 3710 15280 15323 14599 18856 15303 1042 28459 16930 11240 10304 8491 23493 11864 6184 15374 23178 5626 16047 5238 16544 7189 28816 27264 21179 9046 13136 25836 13998 11289 28789 18302 24636 24036 26867 26787 16427 18996 31975 10840 27035 19581 7047 31304 8598 11116 28505 7476 3304 24431 6820 18840 28721 8823 6181 21900 13880 11517 5122 31720 12418 17475 20740 31915 17956 32220 28160 7326 1237 23662 8086 18484 18503 10679 12830 23989 27576 12750 26592 25243 14788 17323 1923 10301 3709 6890 11977 9130 24509 5836 15737 31960 8123 25215 27804 6398 11741 29343 26091 9278 18893 31740 28553 24199 15567 18334 32750 12218 11602 2054 20003 18187 20676 5047 12853 18859 28587 10485 27108 21668 28658 7885 5531 22020 22912 10069 421 317 2320 1845 3997 25292 1340 26214 21542 "
    blades_list = list(blades.split())
    blades_list = [int(i) for i in blades_list]
    blades_list.sort(reverse=True)
    opp_list = list(roudies.split())
    opp_list = [int(j) for j in opp_list]
    opp_list.sort(reverse=True)
    #optimizeTeam(my_team, opp_team)

    #3 6 7 5 3 5 6 2 9 1
    #1 2 3 3 5 5 6 6 7 9
  #Blade >  9 7 6 6 5 5 3 3 2 1
  #Opppppp> 9 7 6 6 6 3 2 2 0 0
  #temp op> 6 6 6 5 3 2 2 0 0

    win_g=0
    temp_opp_list = opp_list[:]
    while T==0:
        for i in range(len(blades_list)):
            #print(temp_opp_list)
            for j in range(len(opp_list)):
                if blades_list[i] > opp_list[j]:
                    temp_opp_list.pop(j)
                    win_g +=1
                    opp_list = temp_opp_list[:]
                    break
            '''for k in range(len(opp_list)):
                if blades_list[i] == opp_list[j]:
                    if len(opp_list) > 1:
                        temp_opp_list.pop(j)
                    else:
                        break
                else:
                    if len(opp_list) > 1:
                        temp_opp_list.pop(j)
                    else:
                        break
            opp_list = temp_opp_list[:]'''
        print(win_g)