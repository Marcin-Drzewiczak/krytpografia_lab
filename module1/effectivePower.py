# Zaimplementuj algorytm (funkcję) efektywnego potęgowania w zbiorze Z∗n.
# Wykorzystaj algorytm iterowanego podnoszenia do kwadratu.
# Dane:n, k∈N, b∈Z∗n
# Wynik:bk∈Z∗n


def effective_power(b, k, n):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y


# print(effective_power(5, 3, 8))
# print(effective_power(16220199497727144388853292719288389348817385984159633033490583062150897614,
#                       137170131566363122825548236710644025089478858806955256122815222401573026049,
#                       274340263132726245651096473421288050178957717613910512245630444803146052099))
# print(effective_power(2403866688370762587352184242744670191479662489869817143091573506181144653550514051791945185487979108973717616292022316623749240485994434557598173783449607360849412910011375383329569946991186718913233779349599430982623385777851530259337543971020206529404547035352583484618462211026682032234245291035727156459618244450476188413406465490694067079755321993171180510550932310295717754282553272969770341308850484398681095025408188695131644392080313383521775927123526599427700243355961482740203655802195360761912900700173803032441571522052878021984446930368680977827872061195151273396213833294624978653127686,
#                       1205105203056077915082972801122733431715692057242312380398252014369417280569205021768910397128826904660304165666576466438346849943906828403216139602668130985862597584796100663902759463852777248803076321623819056079962496000686555223401755052452296548068900592753307159723935714999023687582545005484595340306940550195143263182531063245658588937055664560455134600038420878026675831424063474363273194803492152962168014564474016141478900208401161479326927544178236247629243493565247474128034544094182517697264415517178194539326487604390815896782525168517588047708320980558392389211672782653321208254965158,
#                       18445389417213290016119407664792576331549495678709429640640277332422774559753169042981039707269452568078482017022852304164207452397097130251905079072127610911691791870401874340696766520308109592441564846088088913090789527921754307295377559229163283053980636795073365859918535137440340465081569340168050310381933348387385792297218288020592025608184485077705859391478641573935750404468094274975032497241672567732265500620872791208498980035703066450961831676879542880075377823082273767229274610696616225420412236108684592621351401509932322773487569501949811062490948859598044912948429434645012390928949091))
# print(effective_power(646364623469634716329421551581459444393459634563465364563456387456873465873645876345876345876345876345876345863458763458763485763485763487563845638465837465834658765735646345645856346875,
#                       7268263486823646238468236462384682364586385634856834658634586348658365873645874658734658736458763875638475683765834658346586856348756873465863456,
#                       943923749729479745795479759798579759734597345979578937597359739587398573985793875983759834759735973459873459734985739857359793573598734975983745983745973495734957394579347593847593759734597345973497349857394759347593745934793475973459734957394759374597349573457934759347597345973459734957394579379579579374597359735975173))
# print(effective_power(6438029242480770762029516079455194768492007145281468596426014906016189871039951379196885839922436621616825997924929581374277543019698258251741751826711326118077659511950284427887790474646709622061169776080106652727226216633585807427373860252850929442830311284361608236056098753887394431011113514299642580535755851405584251545506410634813625217863690712561361105743688685508945777352050095791664691549288223844236942741514768185448937730198003384314767815405989770835205498698540267739127576074828218517238306576039006172981865937239533793493010888865668684703024672158056039156003200679552368995006894,
#                       4101531877697825377320246756853939935961867400918119153323843837614296876465531676944127754195445484803573882694790204105610832262108424388354102550671727541886445333854917507113760612589371087675673739974428627763597413239627156424688299366829205076006879520659342135099766979583208409255619539461883209171056863431082927990548226707054184355420337934697039986097734195440271622771705722769471152398544356689646610282579271529014734857936319139711002130396939383863475664591680965793587831396798405995694872631781466615742894537260471961357338961240804799640381205845444865929261855990614700029464446,
#                       15072113879220659349971570720002192823468445944880440474352663966078956906839420872552563479818929174186884166258620035600183044110384173477180778074766461875093665815607748756513338486425271136614266923677715554907039499133347514252736420204623685729653682346129298016732693445180650049135493794571138375552456331624973538738953112333790931946481153045147226030316205756706491598470034615520441920266965003531313792314556565917642005181509989002578271057700672490320555727282061141439212335058665317537832052255892545621033334941015785503297982225380070457160394921114298493441457943997020902914448803))
