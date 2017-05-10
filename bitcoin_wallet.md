###基于椭圆曲线的比特币钱包模型（知识点及代码整理）

***

[TOC]

####背景

***

#####研究的目的和意义

&emsp;&emsp;比特币作为一场货币自由政策的试验，其去中心化的思想和总量恒定的特点，带来很多优点。
&emsp;&emsp;1.从货币经济学的角度来说，比特币打破了以中央机构为信用的机制。按照货币是一般等价物的属性来说，比特币具备货币的三大属性：交易媒介、计价单位、保值工具。从某种意义来说，比特币开启了一个超主权货币的时代。
&emsp;&emsp;2.从去中心化的思想来看，去中心化的比特币，第一次把对第三方机构的信任转移到纯数学理论当中。比特币的源代码是公开的，任何人可以反驳。比特币账簿机制每个人都有，能够避免双重支付问题。去中心化单纯从货币本身来看，很大程度上提高了生产力和生产效率，维护比特币运行的资金远远小于维护金融机构运转产生的资金。
&emsp;&emsp;3.从数据的角度来看。以前沉淀在银行等商业机构中由于种种原因没有公布的数据，浪费了巨大的价值。而在互联网时代，数据即市场，数据可以为市场提供很大的指导意义。比特币是匿名交易，并且交易账本是公开的，账本的分布趋势是可掌握的，因此可以利用比特币的交易数据分析全球经济形势。
&emsp;&emsp;从以上角度来看，比特币可以促进经济的发展。随着比特币交易量的增多，比特币的公私钥对产生方式及安全性引起了广泛关注。在比特币交易中，用户之间是通过地址直接进行交易的，为实现匿名性，每次交易时用户都需要更换交易地址，以及相应的公私钥对，而所有的公私钥对和地址就存放在比特币钱包中。因而研究比特币的钱包模型以及其中公私钥的产生方式，可以加深对比特币的理解，帮助公众安全使用比特币，一定程度上促进比特币的发展。

#####国内外研究现状及发展趋势
    
&emsp;&emsp;现阶段比特币的全球用户约为500万，总市值约220亿人民币。由于比特币的互联网金融属性和技术上的前沿性，从业公司几乎全部是创业公司。据统计，全球范围内获得天使轮以上投资的比特币公司约103家，其中30家位于美国旧金山硅谷。我国较成规模的比特币公司约有20余家，用户约80万人，交易量约占全球70%（由于人民币交易所为免费交易模式，而美元交易所多收取交易手续费，所以此数据仅供参考）。截止到2015年4月，整个行业累计获得风险投资约6亿7千600万美元，其中有4亿美元投资进入了硅谷的比特币初创公司。从产业链角度，目前比特币行业主要有生产（即人们常说的“挖矿”）、交易、存储、应用等四大领域。
&emsp;&emsp;如何对新兴的比特币和电子货币产业进行有效地监管，一直是各国监管部门关注的核心问题。现阶段，欧美主流国家将比特币视作一种投资品或者资产，逐步开始进行法律监管和征税；少部分国家认可比特币的货币地位；极少数国家禁止比特币的使用。
&emsp;&emsp;在未来，比特币的发展存在4个可能方向。一是比特币成为一种全球性的数字资产和投资品，这也是目前比特币在全球扮演的主要角色。二是成为在特定场景下的金融工具。目前在全球范围内不同清算体系之间进行价值传输时，所需时间长、成本高，而比特币作为全球流动的媒介，可以很好地解决这一问题。三是比特币成为一种新型的支付网络，但由于新近的互联网金融公司已经分别将该产业进行升级和创新，因此支付网络的发展尚不明朗。四是创新范围更广、更具有想象力的一种发展趋势。比特币及区块链技术成为一种创新的协议，用于分布式交易、智能合约、去中心化系统、物联网等多个领域，帮助这些领域更快速地发展。
&emsp;&emsp;目前，国际上公认的比较安全、实用的公钥密码体制是基于椭圆曲线上的离散对数难题的椭圆曲线密码体制（ECC）。椭圆曲线密码和其它的公钥密码相比，在相同安全强度下其密钥更短，所以抗攻击性具有绝对的优势，因而引起了密码体制标准制定者以及公钥密码学家的极大兴趣。伴随着ECC算法在全世界的逐渐普及，致力于ECC算法的推广的Certicom公司已经申请了很多有关ECC的专利，现在又组织了SECG (ECC标准化组织)，主要标准有：SEC1和SEC2。IEEE P1363项目分别在1996和1998年公开了在P1363中基于椭圆曲线的公钥密码系统的算法专利，如ECMQV, ECNR等。ANSI X9.62  ANSI X9.63中也涉及了基于椭圆曲线的算法，例如：ECES，ECAES，ECDSA，ECMQV。经过长期的理论研究和科学实践，ECC 得到了迅猛的发展。现在椭圆曲线密码体制不仅是一个重要的理论研究领域，而且已经从理论研究转化为实际可用的密码算法，促使民用安全技术走向产业化。当前，国内外很多生产密码产品的公司都在致力于ECC产品的开发。
&emsp;&emsp;大多密码学家对这种密码体制的安全性及应用前景都抱着乐观的态度，ECC的研究越深入、研究的时间越长，人们对椭圆曲线密码的强度越有信心。密码学界对ECC的青睐，社会各界对ECC的研究及推广，特别是ECC的标准化进程，必将有利于将来对ECC的安全性分析及工程应用的研究。

####正文

***

#####比特币简介

&emsp;&emsp;比特币是由一系列概念和技术作为基础构建的数字货币生态系统。狭义的“比特币”代表系统中的货币单位，用于储存和传输价值。用户主要通过互联网使用比特币系统，当然其他网络也可以使用。比特币协议以各种开源软件的形式实现，这些软件可以在笔记本电脑、智能手机等多种设备上运行，让用户方便地接入比特币系统。
&emsp;&emsp;比特币可以做传统货币能做的所有事，例如买卖商品、给个人或组织汇款、贷款。用户可以在专门的交易所里买卖比特币或兑换其他货币。在一定意义上，比特币才是互联网货币的完美形态。因为它具有快捷、安全、无国界的特性。
&emsp;&emsp;不同于传统货币，比特币是完全虚拟的。它不但没有实体，本质上也没有一种虚拟物品代表比特币。比特币隐含在收发币的转账记录中。用户只要有证明其控制权的密钥，用密钥解锁，就可以发送比特币。这些密钥通常存储在计算机的数字钱包里。拥有密钥是使用比特币的唯一条件，这让控制权完全掌握在每个人手中。
&emsp;&emsp;比特币是一个分布式的点对点网络系统。因此没有“中央”服务器，也没有中央发行机构。比特币是通过“挖矿”产生的，挖矿就是验证比特币交易的同时参与竞赛来解决一个数学问题。任何参与者（比如运行一个完整协议栈的人）都可以做矿工，用他们的电脑算力来验证和记录交易。平均每10分钟就有人能验证过去这10分钟发生的交易，他将会获得新币作为工作回报。本质上，挖矿把央行的货币发行和结算功能进行分布式，用全球化的算力竞争来取代对中央发行机构的需求。
&emsp;&emsp;比特币系统包含调节挖矿难度的协议。挖矿——在比特币网络中成功写入一个区块交易——的难度是动态调整的，保证不管有多少矿工（多少CPU）挖矿，平均每10分钟只有一个矿工成功。
&emsp;&emsp;比特币协议还规定，每四年新币的开采量减半，同时限制比特币的最终开采总量为2,100万枚。这样，流通中的比特币数量非常接近一条曲线，并将在2140年比特币将达到2,100万枚。由于比特币的开采速度随时间递减，从长期来看，比特币是一种通货紧缩货币。此外，不能通过“印刷”新比特币来实现“通货膨胀”。
&emsp;&emsp;比特币是一种协议、一种网络、一种分布式计算创新的代名词。比特币是这种创新的首次实际应用。作为一个开发者，我看比特币之于货币就像看到当年的互联网，一个通过分布式计算来传播价值和保障数字资产所有权的网络。

#####比特币简单原理

&emsp;&emsp;与传统银行和支付系统不同，比特币系统是以去中心化信任为基础的。由于比特币网络中不存在中央权威信任机构，“信任”成为了比特币用户之间存在的一种突出特性。简单来说，比特币交易告知全网：比特币的持有者已授权把比特币转帐给其他人。而新持有者能够再次授权，转移给该比特币所有权链中的其他人，产生另一笔交易来花掉这些比特币，后面的持有者在花费比特币也是用类似的方式。交易也包含了每一笔被转移的比特币（输入）的所有权证明，它以所有者的数字签名形式存在，并可以被任何人独立验证。在比特币术语中，“消费”指的是签署一笔交易：转移一笔以前交易的比特币给以比特币地址所标识的新所有者。交易是将钱从交易输入移至输出。输入是指钱币的来源，通常是之前一笔交易的输出。交易的输出则是通过关联一个密钥的方式将钱赋予一个新的所有者。目的密钥被称为是安全锁（Encumbrance）。这样就给资金强加了一个要求：有签名才能在以后的交易中赎回资金。一笔交易的输出可以被当做另一笔新交易的输入，这样随着钱从一个地址被移动到另一个地址的同时形成了一条所有权链
*详细交易步骤：*

1. *获取正确的输入*
用户Alice的钱包查询她的比特币地址中未消费的金额，即用户的所剩余额。完整客户端含有整个区块链中所有交易的所有未消费输出副本。这使得钱包即能拿这些输出构建交易，又能在收到新交易时很快地验证其输入是否正确。
2. *创建交易输出*
交易的输出会被创建成为一个包含这笔数额的脚本的形式，只能被引入这个脚本的一个解答后才能兑换。简单点说就是，Alice的交易输出会包含一个脚本，这个脚本说 “这个输出谁能拿出一个签名和Bob的公开地址匹配上，就支付给谁”。因为只有Bob的钱包的私钥可以匹配这个地址，所以只有Bob的钱包可以提供这个签名以兑换这笔输出。因此Alice会用需要Bob的签名来包装一个输出。
3. *交易传送*
这个被Alice钱包应用创建的交易大小为258字节，包含了金额未来所属需要的全部信息。现在，这个交易必须要被传送到比特币网络中以成为分布式账簿（区块链）的一部分。比特币网络是由参与的比特币客户端联接几个其他比特币客户端组成的P2P网络。因此，这个交易迅速地从P2P网络中传播开来，几秒内就能到达大多数节点。
4. *比特币挖矿*
这个交易现在在比特币网络上传播开来。然后被一个称为挖矿的过程验证且加到一个区块中之后，这个交易才会成为这个共享账簿（区块链）的一部分。
5. *消费这笔交易*
Bob现在可以将此交易的结果信息作为输入，创建新的所有权为其他人的交易，返回步骤一

#####钱包
   
&emsp;&emsp;比特币钱包使使用者可以检查、储存、花费其持有的比特币，其形式多种多样，功能可繁可简，它可以是遵守比特币协议运行的各种工具，如电脑用户端、手机用户端、网站服务、专用设备，也可以只是存储著比特币私密金钥的介质，如一张纸、一段暗号、一个快闪随身碟、一个文本文档，因为只要掌握比特币的私密金钥，就可以处置其对应地址中包含的比特币。
&emsp;&emsp;比特币的所有权是通过数字密钥、比特币地址和数字签名来确立的。数字密钥实际上并不是存储在网络中，而是由用户生成并存储在一个文件或简单的数据库中，称为钱包。存储在用户钱包中的数字密钥完全独立于比特币协议，可由用户的钱包软件生成并管理，而无需区块链或网络连接。密钥实现了比特币的许多有趣特性，包括去中心化信任和控制、所有权认证和基于密码学证明的安全模型。
&emsp;&emsp;每笔比特币交易都需要一个有效的签名才会被存储在区块链。只有有效的数字密钥才能产生有效的数字签名，因此拥有比特币的密钥副本就拥有了该帐户的比特币控制权。密钥是成对出现的，由一个私钥和一个公钥所组成。公钥就像银行的帐号，而私钥就像控制账户的PIN码或支票的签名。比特币的用户很少会直接看到数字密钥。一般情况下，它们被存储在钱包文件内，由比特币钱包软件进行管理。
&emsp;&emsp;在比特币系统中，我们用公钥加密创建一个密钥对，用于控制比特币的获取。密钥对包括一个私钥，和由其衍生出的唯一的公钥。公钥用于接收比特币，而私钥用于比特币支付时的交易签名。
&emsp;&emsp;公钥和私钥之间的数学关系，使得私钥可用于生成特定消息的签名。此签名可以在不泄露私钥的同时对公钥进行验证。
&emsp;&emsp;支付比特币时，比特币的当前所有者需要在交易中提交其公钥和签名（每次交易的签名都不同，但均从同一个私钥生成）。比特币网络中的所有人都可以通过所提交的公钥和签名进行验证，并确认该交易是否有效，即确认支付者在该时刻对所交易的比特币拥有所有权。
    
* ######私钥
    
    &emsp;&emsp;比特币私密金钥用于证明比特币的拥有者。私密金钥可以给消息（最常见的，花费比特币的消息）签名，以证明消息的发布者是相应地址的所有者。掌握私密金钥就等于掌握其对应地址中存放的比特币，所以私密金钥必须保密。比特币私密金钥通常由51位元或52位元字元表示，其编码方式与比特币地址相似。51位元标记法由数字“5”开头，52位标记法由“K”或“L”开头。比特币地址是由比特币公开金钥进行杂凑运算得出的，公开金钥是可以通过私密金钥推算出的。所以掌握私密金钥就可以推算出私密金钥对应的地址（不可逆）。
    &emsp;&emsp;生成密钥的第一步也是最重要的一步，是要找到足够安全的熵源，即随机性来源。生成一个比特币私钥在本质上与“在1到2<sup>256</sup>之间选一个数字”无异。只要选取的结果是不可预测或不可重复的，那么选取数字的具体方法并不重要。比特币软件使用操作系统底层的随机数生成器来产生256位的熵（随机性）。通常情况下，操作系统随机数生成器由人工的随机源进行初始化，也可能需要通过几秒钟内不停晃动鼠标等方式进行初始化。对于真正的偏执狂，可以使用掷骰子的方法，并用铅笔和纸记录。
    &emsp;&emsp;更准确地说，私钥可以是1和n-1之间的任何数字，其中n是一个常数（n=1.158*10<sup>77</sup>，略小于2<sup>256</sup>），并由比特币所使用的椭圆曲线的阶所定义。通常是由随机算法生成的，说白了，就是一个巨大的随机整数，256位、32字节。大小介于1 ~ 0xFFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFE BAAE DCE6 AF48 A03B BFD2 5E8C D036 4141之间的数，都可以认为是一个合法的私钥。要生成这样的一个私钥，我们随机选择一个256位的数字，并检查它是否小于n-1。从编程的角度来看，一般是通过在一个密码学安全的随机源中取出一长串随机字节，对其使用SHA256哈希算法进行运算，这样就可以方便地产生一个256位的数字。如果运算结果小于n-1，我们就有了一个合适的私钥。否则，我们就用另一个随机数再重复一次。
    使用[pybitcointools库](https://github.com/vbuterin/pybitcointools)来生成随机私钥代码：
    ```python
    valid_private_key = False
    while not valid_private_key:
        private_key = bitcoin.random_key()
        decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
        valid_private_key =  0 < decoded_private_key < bitcoin.N
    print ("私钥（十六进制）：      ", private_key)
    print ("私钥（十进制）：        ", decoded_private_key)
    ```
    随机私钥生成结果：
    >私钥（十六进制）：       c991e2ee4e3c30365b2ae811c09a57c7b3555245aa1daf8531c9a97e900e74f9
    >私钥（十进制）：         91172641609010210032828285652639569129132670351783936583713707728470677550329

    使用[pybitcointools库](https://github.com/vbuterin/pybitcointools)来生成特定私钥代码：
    ```python
    from bitcoin import *
    priv = sha256('some big long brainwallet password')
    print (priv)
    ```
    特定私钥生成结果：
    >'57c617d9b4e1f7af6ec97ca2ff57e94a28279a7eedd4d12a99fa11170e94f5a4'
    
    <br/>
    *私钥表示法（编码格式）：*
    >|种类|Base58格式|描述|
    >|-|-|-|
    >|Hex            |None    |64 hexadecimal digits
    >|Hex-compressed |None    |64 hexadecimal digits and suffix 0x01
    >|WIF            |5       |Base58Check encoding: Base58 with version prefix of 128(0x80) and 32-bit checksum
    >|WIF-compressed |K or L  |As above, with added suffix 0x01 before encoding

    &emsp;&emsp;实际上“压缩格式私钥”是一种名称上的误导，因为当一个私钥被使用WIF压缩格式导出时，不但没有压缩，而且比“非压缩格式”私钥长出一个字节。这个多出来的一个字节是私钥被加了后缀01，用以表明该私钥是来自于一个较新的钱包，只能被用来生成压缩的公钥。私钥是非压缩的，也不能被压缩。“压缩的私钥”实际上只是表示“用于生成压缩格式公钥的私钥”，而“非压缩格式私钥”用来表明“用于生成非压缩格式公钥的私钥”。为避免更多误解，应该只可以说导出格式是“WIF压缩格式”或者“WIF”，而不能说这个私钥是“压缩”的。
    &emsp;&emsp;要注意的是，这些格式并不是可互换使用的。在较新的实现了压缩格式公钥的钱包中，私钥只能且永远被导出为WIF压缩格式（以K或L为前缀）。对于较老的没有实现压缩格式公钥的钱包，私钥将只能被导出为WIF格式（以5为前缀）导出。这样做的目的就是为了给导入这些私钥的钱包一个信号：到底是使用压缩格式公钥和比特币地址去扫描区块链，还是使用非压缩格式公钥和比特币地址。
    &emsp;&emsp;如果一个比特币钱包实现了压缩格式公钥，那么它将会在所有交易中使用该压格式缩公钥。钱包中的私钥将会被用来生成压缩格式公钥，压缩格式公钥然后被用来生成交易中的比特币地址。当从一个实现了压缩格式公钥的比特币钱包导出私钥时，钱包导入格式（WIF）将会被修改为WIF压缩格式，该格式将会在私钥的后面附加一个字节大小的后缀01。最终的Base58Check编码格式的私钥被称作WIF（“压缩”）私钥，以字母“K”或“L”开头。而以“5”开头的是从较老的钱包中以WIF（非压缩）格式导出的私钥。


* ######公钥

    &emsp;&emsp;通过椭圆曲线算法可以从私钥计算得到公钥，这是不可逆转的过程：`K = k * G`。其中`k`是私钥，`G`是被称为生成点的常数点，而`K`是所得公钥。其反向运算，被称为“寻找离散对数”——已知公钥`K`来求出私钥`k`——是非常困难的，就像去试验所有可能的k值，即暴力搜索。
    比特币使用了`secp256k1`标准所定义的一条特殊的椭圆曲线和一系列数学常数。
    >y<sup>2</sup>mod p = (x<sup>3</sup> + 7) mod p
    p = 2<sup>256</sup> – 2<sup>32</sup> – 2<sup>9</sup> – 2<sup>8</sup> – 2<sup>7</sup> – 2<sup>6</sup> – 2<sup>4</sup> – 1
    
    公钥`K`被定义为一个点`K = (x, y)`
    使用[pybitcointools库](https://github.com/vbuterin/pybitcointools)来生成特定公钥代码：
    ```python
    from bitcoin import *
    priv = sha256('some big long brainwallet password')
    pub = privtopub(priv)
    print (pub)
    ```
    特定公钥钥生成结果：
    >'0420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9'

    &emsp;&emsp;公钥是在椭圆曲线上的一个点，由一对坐标（x，y）组成。公钥通常表示为前缀04紧接着两个256比特的数字。其中一个256比特数字是公钥的x坐标，另一个256比特数字是y坐标。前缀04是用来区分非压缩格式公钥，压缩格式公钥是以02或者03开头。
    <br/>
    *公钥表示法（编码格式）：*
    >|种类|前缀（Hex）|格式（Hex）|举例|
    >|-|-|-|-|
    >|Hex|04|04xy|04F028892BAD7ED57D2FB57BF33081D5CFCF6F9ED3D3D7F159C2E2FFF579DC341A07CF33DA18BD734C600B96A72BBC4749D5141C90EC8AC328AE52DDFE2E505BDB
    >|Hex-compressed|02|02x（y为偶数）|0266CC7B651B7D60E84A902919B60BB4794B19CEA007D517155C85B40E2A37B529
    >|Hex-compressed|03|03x（y为奇数）|03F028892BAD7ED57D2FB57BF33081D5CFCF6F9ED3D3D7F159C2E2FFF579DC341A

* ######地址
    
    &emsp;&emsp;地址是为了人们交换方便而弄出来的一个方案，因为公钥太长了*（130字符串（520bits）或66字符串（264bits））*。地址长度为25字节*（版本前缀1字节+公钥Hash160产生20字节+双哈希校验码前4字节）*，通过转为Base58Check编码后，变为34或35个字符，即用来交易时发给别人的地址。
    &emsp;&emsp;为了更简洁方便地表示长串的数字，许多计算机系统会使用一种以数字和字母组成的大于十进制的表示法。例如，传统的十进制计数系统使用0-9十个数字，而十六进制系统使用了额外的 A-F 六个字母。一个同样的数字，它的十六进制表示就会比十进制表示更短。更进一步，Base64使用了26个小写字母、26个大写字母、10个数字以及两个符号（例如“+”和“/”），用于在电子邮件这样的基于文本的媒介中传输二进制数据。Base64通常用于编码邮件中的附件。Base58是一种基于文本的二进制编码格式，用在比特币和其它的加密货币中。这种编码格式不仅实现了数据压缩，保持了易读性，还具有错误诊断功能。Base58是Base64编码格式的子集，同样使用大小写字母和10个数字，但舍弃了一些容易错读和在特定字体中容易混淆的字符。具体地，Base58不含Base64中的0（数字0）、O（大写字母o）、l（小写字母L）、I（大写字母i），以及“+”和“/”两个字符。简而言之，Base58就是由不包括（0，O，l，I）的大小写字母和数字组成。
    >比特币的Base58字母表：
    >123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz

    &emsp;&emsp;Base58Check是一种常用在比特币中的Base58编码格式，增加了错误校验码来检查数据在转录中出现的错误。校验码长4个字节，添加到需要编码的数据之后。校验码是从需要编码的数据的哈希值中得到的，所以可以用来检测并避免转录和输入中产生的错误。使用Base58check编码格式时，编码软件会计算原始数据的校验码并和结果数据中自带的校验码进行对比。二者不匹配则表明有错误产生，那么这个Base58Check格式的数据就是无效的。例如，一个错误比特币地址就不会被钱包认为是有效的地址，否则这种错误会造成资金的丢失。由于存在公钥有两种形式，那么一个公钥便对应两个地址。这两个地址都可由同一私钥签署交易。
    *详细步骤图解：*
    ![Load Fail](http://zhibimo.com/read/wang-miao/mastering-bitcoin/Images/Fig405.png)
    其中由公钥hash编码为base58步骤：
    ![Load Fail](http://zhibimo.com/read/wang-miao/mastering-bitcoin/Images/Fig406.png)
    >Base58Check版本前缀和编码后的结果:
    >
    >|种类|版本前缀 (hex)|Base58格式|
    >|-|-|-|
    >|Bitcoin Address            | 0x00     | 1         |
    >|Pay-to-ScriptHash Address  | 0x05     | 3         |
    >|Bitcoin Testnet Address    | 0x6F     | m or n    |
    >|Private Key WIF            | 0x80     | 5, K or L |
    >|BIP38 Encrypted Private Key|0x0-142   | 6P        |
    >|BIP32 Extended Public Key| 0x0488B21E | xpub      |

    使用[pybitcointools库](https://github.com/vbuterin/pybitcointools)来生成特定公钥代码：
    ```python
    from bitcoin import *
    priv = sha256('some big long brainwallet password')
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    print (addr)
    ```
    地址（非压缩公钥）生成结果：
    >'1CQLd3bhw4EzaURHbKCwM5YZbUQfA4ReY6'

* ######随机钱包

    &emsp;&emsp;在最早的一批比特币客户端中，钱包只是随机生成的私钥集合。这种类型的钱包被称作零型非确定钱包。举个例子，比特币核心客户端预先生成100个随机私钥，从最开始就生成足够多的私钥并且每把钥匙只使用一次。这种类型的钱包有一个昵称“Just a Bunch Of Keys（一堆私钥）”简称JBOK。这种钱包现在正在被确定性钱包替换，因为它们难以管理、备份以及导入。随机钥匙的缺点就是如果你生成很多，你必须保存它们所有的副本。这就意味着这个钱包必须被经常性地备份。每一把钥匙都必须备份，否则一旦钱包不可访问时，钱包所控制的资金就付之东流。这种情况直接与避免地址重复使用的原则相冲突——每个比特币地址只能用一次交易。

* ######分层确定钱包

    &emsp;&emsp;确定性钱包被开发成更容易从单个“种子”中生成许多关键的钥匙。最高级的来自确定性钱包的形是通过BIP0032标准生成的 the hierarchical deterministic wallet or HD wallet defined。分层确定性钱包包含从数结构所生成的钥匙。这种母钥匙可以生成子钥匙的序列。这些子钥匙又可以衍生出孙钥匙，以此无穷类推。
    *详细步骤图解：*
    创建主密钥：
    ![Load Fail](http://zhibimo.com/read/wang-miao/mastering-bitcoin/Images/Fig410.png)
    <br/>
    创建子密钥：
    ![Load Fail](http://zhibimo.com/read/wang-miao/mastering-bitcoin/Images/Fig411.png)
    &emsp;&emsp;改变索引可以让我们延长母密钥以及创造序列中的其他子密钥。比如子0，子1，子2等等。每一个母密钥可以右20亿个子密钥。向密码树下一层重复这个过程，每个子密钥可以依次成为母密钥继续创造它自己的子密钥，直到无限代。

#####代码实现

* ######产生一个密钥对及比特币地址
    
    ```python
    import bitcoin  

    # Generate a random private key***********************************************************************
    valid_private_key = False
    while not valid_private_key:
        private_key = bitcoin.random_key()
        decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
        valid_private_key =  0 < decoded_private_key < bitcoin.N    

    print ("私钥（十六进制）：      ", private_key)
    print ("私钥（十进制）：        ", decoded_private_key) 

    # Convert private key to WIF format
    wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
    print ("私钥（WIF格式）：       ", wif_encoded_private_key)    

    # Add suffix "01" to indicate a compressed private key
    compressed_private_key = private_key + '01'
    print ("压缩私钥（十六进制）：  ", compressed_private_key) 

    # Generate a WIF format from the compressed private key (WIF-compressed)
    wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
    print ("压缩私钥（WIF格式）：   ", wif_compressed_private_key)   

    # Generate a public key*******************************************************************************
    # Multiply the EC generator point G with the private key to get a public key point
    public_key = bitcoin.fast_multiply(bitcoin.G,decoded_private_key)
    print ("公钥十进制坐标(x,y)：   ", public_key)  

    # Encode as hex, prefix 04
    hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex')
    print ("公钥十六进制非压缩：    ", hex_encoded_public_key)    

    # Compress public key, adjust prefix depending on whether y is even or odd
    (public_key_x, public_key_y) = public_key
    if (public_key_y % 2) == 0:
         compressed_prefix = '02' 
    else:
         compressed_prefix = '03'
    hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
    print ("公钥十六进制压缩：      ", hex_compressed_public_key)    

    # Generate bitcoin address from public key************************************************************
    print ("比特币地址(b58check)：  ", bitcoin.pubkey_to_address(public_key)) 

    # Generate compressed bitcoin address from compressed public key
    print ("压缩公钥地址(b58check)：", bitcoin.pubkey_to_address(hex_compressed_public_key))
    ```
    结果：
    >私钥（十六进制）：       9fb47fe943a00279a3742c0773d54436b5763b6edbab7a3e49f43f43855b2185
    >私钥（十进制）：         72236658206974828479883065078493895322112559805816672978630985027031286882693
    >私钥（WIF格式）：        5K2d2tSLbv7AF2cCgWtTFjn63kzkVxN19symvgxiahxAXNb1oMi
    >压缩私钥（十六进制）：   9fb47fe943a00279a3742c0773d54436b5763b6edbab7a3e49f43f43855b218501
    >压缩私钥（WIF格式）：    L2aA3L2qX7QBnv6NZQv6t3p1HBBtzoMhgC1bHyNvXmkV2sgkwaNz
    >公钥十进制坐标(x,y)：    (75994727348152113011574975086469717444527451212545062406630381125606976246234, 68696992193901212880533605255299539612603103440712869710273413670807007624489)
    >公钥十六进制非压缩：     04a8037dccfeec5c9f9330b466360928fd72bd34b7244458cffaa375674a77d1da97e11ea3cb1efbe96b1fc24395b7e890dbe1b101f2535067543ca821f8077d29
    >公钥十六进制压缩：       03a8037dccfeec5c9f9330b466360928fd72bd34b7244458cffaa375674a77d1da
    >比特币地址(b58check)：   1AicLLBQwjzJLZgB1FBeWNQ6sBps5j62FV
    >压缩公钥地址(b58check)： 16jjvxaezxDrziZgRNNNyZRYC1JbGNRSjD

* ######生成多个密钥按顺序连接

    ```python
    import bitcoin
    import hashlib  

    # Generate a random private key as a root seed********************************************************
    valid_private_key_seed = False
    while not valid_private_key_seed:
        private_key_seed = bitcoin.random_key()
        decoded_private_key_seed = bitcoin.decode_privkey(private_key_seed, 'hex')
        valid_private_key_seed =  0 < decoded_private_key_seed < bitcoin.N
    print ("随机种子256 bits（十六进制）： ", private_key_seed)    

    # 由种子生成主私钥、主公钥、比特币地址
    hash512_sequence = hashlib.sha512(private_key_seed.encode('utf-8')).hexdigest()
    master_private_key = hash512_sequence[:64]
    main_chain_code = hash512_sequence[64:]
    master_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(master_private_key, 'hex')),'hex')
    master_address = bitcoin.pubkey_to_address(master_public_key)
    print ("主私钥（十六进制）：           ", master_private_key)
    print ("主公钥（非压缩十六进制）：     ", master_public_key)
    print ("相应比特币地址(b58check)：     ", master_address)   

    # 分层确定性钱包使用CKD（child key derivation）方程去从母密钥衍生出子密钥
    # 生成3个子密钥
    index_0 = '0000'
    index_1 = '0001'
    index_2 = '0002'    

    child_0_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_0).encode('utf-8')).hexdigest()
    child_0_private_key = child_0_hash512_sequence[:64]
    child_0_chain_code = child_0_hash512_sequence[64:]
    child_0_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_0_private_key, 'hex')),'hex')
    child_0_address = bitcoin.pubkey_to_address(child_0_public_key)
    print ("索引0子私钥（十六进制）：      ", child_0_private_key)
    print ("索引0子公钥（非压缩十六进制）：", child_0_public_key)
    print ("相应比特币地址(b58check)：     ", child_0_address)  

    child_1_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_1).encode('utf-8')).hexdigest()
    child_1_private_key = child_1_hash512_sequence[:64]
    child_1_chain_code = child_1_hash512_sequence[64:]
    child_1_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_1_private_key, 'hex')),'hex')
    child_1_address = bitcoin.pubkey_to_address(child_1_public_key)
    print ("索引1子私钥（十六进制）：      ", child_1_private_key)
    print ("索引1子公钥（非压缩十六进制）：", child_1_public_key)
    print ("相应比特币地址(b58check)：     ", child_1_address)  

    child_2_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_2).encode('utf-8')).hexdigest()
    child_2_private_key = child_2_hash512_sequence[:64]
    child_2_chain_code = child_2_hash512_sequence[64:]
    child_2_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_2_private_key, 'hex')),'hex')
    child_2_address = bitcoin.pubkey_to_address(child_2_public_key)
    print ("索引2子私钥（十六进制）：      ", child_2_private_key)
    print ("索引2子公钥（非压缩十六进制）：", child_2_public_key)
    print ("相应比特币地址(b58check)：     ", child_2_address)
    ```
    结果：
    >随机种子256 bits（十六进制）：  b8a70fd89b23c1b7224400d33d7e0842c2986ca4504d5ef138a1102add566100
    >主私钥（十六进制）：            fe7de1b50c659256296e079e1651402b6b585a8c20cdc86e63273664f55b3ed7
    >主公钥（非压缩十六进制）：      0453213ac3039de3e27e9ac743f3e1dff7d8bc8ddf76ae56f23df97c132c39d774fcf8163f9e6775eaf3669fbcbc7b35b43d22f7f36c7d126ddefb2d30e8721fa6
    >相应比特币地址(b58check)：      1EEEVcsvmBoJFz1iMMxh1YaZu7YJodN3vu
    >索引0子私钥（十六进制）：       c98f46803bdd62d23914986ed35e1b1dc0234a45b35b35a00dd43620e84be5a6
    >索引0子公钥（非压缩十六进制）： 04372f42bb782edcf27ff45baa0908f08d22cd00cc7c59fa2cbc6e46ebdb555956dee86d0610ed884d9b1f5a3298183b0e29cbdd5311d8051a54bc505cde3b7b9c
    >相应比特币地址(b58check)：      1LrsCjEb6Kx9KZVLE77Vi2skAW22oJbPSa
    >索引1子私钥（十六进制）：       5a6b0c0ffc4c663c78b1d451ec0360fc8efb5ea715f86b0b36e47074aebde32c
    >索引1子公钥（非压缩十六进制）： 04309d39ff392ccd3a3f629253263d7a6349f43ab88e27a2ab1349b0f2f61833fd0457a4dd57552b7612a24eed1be06d5159d657965ae95699184577c654ef5d6e
    >相应比特币地址(b58check)：      1Ghy4wN33VJtZaJns3ntem8z8oE6RjD46b
    >索引2子私钥（十六进制）：       471213c7ada101234f35d8a1ec6529187e04382430a267c7b52bc8432c48c1bf
    >索引2子公钥（非压缩十六进制）： 044ab510435cbfd6c2029364ac28795040b3c0ecaf5b157b04b521db94e6ddfcd14f8fc054185e6a356bb762f7c17c39221d2cf8d1b57ef17f065e14a42a035cf6
    >相应比特币地址(b58check)：      1BRE2AAjQcM9RjTaY8xpFhd66e7Ae79ABQ

* ######GUI设计
    
    \*
    \*
    \*  尚未完成
    \*
    \*

####参考

***

[1]：[Mastering Bitcoin——Andreas M Antonopoulos（中译版）](http://zhibimo.com/read/wang-miao/mastering-bitcoin/)
[2]：[pybitcointools——Vitalik Buterin](https://github.com/vbuterin/pybitcointools)
[3]：[比特币基础知识原理讲解](http://jingyan.baidu.com/article/bad08e1ebac68f09c9512143.html)
[4]：[比特币——开源的P2P货币](https://bitcoin.org/zh_CN/)
[5]：[Bitcoin Wiki](https://en.bitcoin.it/wiki/Main_Page)
[6]：
