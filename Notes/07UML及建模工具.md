---
title: "软件过程与工具——UML及建模工具"
date: 2022-01-01 22:38:38
tags: HIT Software Process and Tools
mathjax: true
---

# UML及建模工具

## 一. UML简介

### 1. 模型及其作用

- ***模型就是现实的简单化***

- **模型的目的或用途：**模型是为了更好地理解正在开发的系统：系统**可视化**、详细说明系统的**结构或行为**（e.g. 静态/动态结构、行为 $\Rightarrow$ 时序描写）、指导构造系统的**模板**、决策进行**文档化**、构建物理实体前先测试、与客户交流、降低**复杂度**。

- **面向对象的建模：**软件系统用**对象（类）**作为其构造单元（块）；class属性（静态）、方法（动态）
  - 从**问题空间或解空间**的**词汇**中找出**对象**
  - 类是对具有共同性质的一组对象的描述

### 2. UML介绍

***UML——Unified Modeling Language 统一建模语言***

UML 是一种对软件系统的制作过程/产出物进行下述工作的描述语言，这些工作包括：**可视化（visualizing）、详述 （specifying）、构造 （constructing）、文档化（documenting）**。

统一标准：UML已成为**面向对象的标准化**的统一的建模语言

**UML与代码的关系**：编码是实现一个系统，UML是对一个模型建立模型，一些工具（比如Rational Rose）可以根据UML建立的模型来产生java、C++或其他程序语言代码框架。

**UML的构成：**视图（Views）、图（Diagrams）、模型元素、通用机制

### 3. UML工具

Microsoft Visio、IBM Rational Rose、I-Logix、POPKIN、ORACLE、Borland、StarUML、

### 4. 视图（Views）

三视图

***视图***是表达系统某一方面特征的 UML 建模元素的子集，它是由一个或者多个图组成的**对系统某个角度的抽象**。

![image-20211223120418441](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223120418441.png)

- ***Use Case View（用例视图）***
  - 用途：描述系统应该具备的功能，被称为参与者（执行者）的***外部用户所能观察到的功能***
  - 其他几个视图的核心，直接驱动其他视图的开发
  - 包含UML图：***用例图***
  - 使用者：分析人员
- ***Logical View（逻辑视图）***
  - 用途：描述用例图中提出的***系统功能的实现***
  - 包含UML图：***静态结构（类图、对象图），动态协作关系（状态图、时序图、协作图、活动图）***
  - 使用者：分析人员、设计人员、开发人员
- ***Process View（进程视图）***
  - 用途：考虑***资源***的有效利用、***代码的并行执行***以及系统环境中***异步事件***的处理
  - 解决在并发系统中存在的**通信和同步问题**
  - 包含UML图：***状态图、协作图、组件图、活动图***
  - 使用者：开发人员、系统集成人员
- ***Implementation View（实现视图）***
  - 用途：描述系统的***实现模块***以及它们之间的***依赖关系***
  - 包含UML图：***组件图***
  - 使用者：开发人员
- ***Deployment View（部署视图）***
  - 用途：显示系统的***物理部署（物理设备）***，并描述位于节点实例上的运行组件实例的部署情况
  - 包含UML图：***部署图***
  - 使用者：开发人员、系统集成人员、测试人员



***<u>UML中的模型图</u>***：类图（class diagram）、对象图（object diagram）、用例图（use case diagram）、时序图（sequence diagram）、协作图（collaboration diagram）、状态图（statechart diagram）、活动图（activity diagram）、组件图（component diagram）、部署图（deployment diagram）

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223125337619.png" alt="image-20211223125337619" style="zoom:80%;" />



UML中的关系：**关联、依赖、泛化、实现、聚合**

- ***关联***![image-20211223130359738](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130359738.png)
- ***依赖*** ![image-20211223130432036](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130432036.png)
- ***泛化*** ![image-20211223130445435](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130445435.png)
- ***实现*** ![image-20211223130457344](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130457344.png)
- ***聚合/组合*** ![image-20211223130509537](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130509537.png)



UML 模型中最**基本的结构化事物**，包括：***类、接口、协作、用例、活动类、组件、节点***

- ***类***
  - 对相同属性、方法、关系和语义的对象的抽象
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223125737888.png" alt="image-20211223125737888" style="zoom:50%;" />
- ***接口***
  - **类或组件**提供特定服务的一组操作的集合
  - 描述了类或组件的**对外可见的动作**
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223125924946.png" alt="image-20211223125924946" style="zoom: 33%;" />
- ***协作***
  - 定义了交互操作
  - 代表构成系统的模式的实现
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130014686.png" alt="image-20211223130014686" style="zoom:50%;" />
- ***用例***
  - 描述系统对一个特定角色执行一系列动作
  - 组织动作事件
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130100994.png" alt="image-20211223130100994" style="zoom:50%;" />
- ***活动类（对象）***
  - 有一个或多个进程或线程的类
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130146423.png" alt="image-20211223130146423" style="zoom:50%;" />
- ***组件***
  - 实现了物理上可替换的系统部分
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130219987.png" alt="image-20211223130219987" style="zoom:50%;" />
- ***节点***
  - 在运行时存在的一个物理元素
  - 代表一个可计算的资源
  - 通常占用一些内存和具有处理能力
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223130320177.png" alt="image-20211223130320177" style="zoom:67%;" />

## 二. 用例图

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/5CD16393087937A75137A308A25D4B97.png" alt="img" style="zoom: 50%;" />

### 1. 用例图简介

用例图应用在软件开发的**需求分析阶段**，描述了系统的功能以及如何使用一个系统

用例图显示谁将是相关的***用户***、用户希望***系统提供什么服务***以及***用户需要为系统提供的服务***

***<u>用例图类型</u>***

- **业务用例图** $\Rightarrow$ 边界是组织——用例是期望、服务
- **系统用例图**  $\Rightarrow$ 边界是系统/子系统——用例是子系统、模块、功能

### 2. 用例图的组成

用例图主要包含以下 6 个元素：**参与者（Actor）、用例（Use Case）、关联关系（Association）、包含关系（Include）、扩展关系（Extend）、泛化关系（Generalization）**

### 3. 参与者、用例、事件流

#### 3.1 参与者（Actor）

***<u>参与者的概念</u>***：参与者是***系统外部的一个实体***，参与用例的执行过程，参与者由参与用例时所担当的***角色表示***，每个参与者可以参加**一个或多个用例**

***参与者的种类：***参与者可以是系统**用户**（真实的人，即user，**最常见**的参与者，存在于每一个系统，按角色命名）、**时间代理人（timer）**、交互的**其他系统**（外部程序），其他如硬件设备、外部设备和外部数据库等。

**总之参与者不一定是人** ，但参与者由”***角色***“表示**而不是特定的人或事**。



***<u>先定系统边界</u>*** $\Rightarrow$ 寻找系统参与者，参与者对系统而言总是外部的

参与者可以**直接或间接**地同系统交互或使用系统提供的服务以完成某件事件

一个人或事物在与系统发生交互时，可以**扮演多个角色**



***启动者和支持者（协作者）***

- **启动者是用例的主要服务对象**
- **另一类是扮演支持者角色的参与者**
- <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223134646388.png" alt="image-20211223134646388" style="zoom: 80%;" />



参与者之间可以具有***泛化关系***，使用泛化关系来描述多个参与者之间的**公共行为**

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223134750808.png" alt="image-20211223134750808" style="zoom: 67%;" />

#### 3.2 用例与事件流

***用例的概念***：用例是**外部可见的系统功能单元**，不揭露系统内部构造的前提下定义连贯的行为，不是需求或功能的说明

用例的表示：简单名（simple name）<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223141700254.png" alt="image-20211223141700254" style="zoom:50%;" />、路径名（Path name)<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223141709224.png" alt="image-20211223141709224" style="zoom:50%;" />

**用例分析处于系统的需求分析阶段，这个阶段应该尽量避免考虑系统的细节问题**

**实际建立系统，则需要更加具体的细节，这些细节写在用例对应的事件流文件中**

值得注意的是事件流描述的也是系统***”做什么“***，而不是”怎么做“



***事件流文件组成***（常见的事件流描述方法是一个表格）

- 简要说明（用例相关、参与者）
- 前提条件
- 后置条件
- 事件流程（主事件流、其他事件流、错误流）

### 4. 用例间的关系

- ***关联关系：***参与者与用例之间的关系
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223142528579.png" alt="image-20211223142528579" style="zoom: 50%;" />
- ***包含关系：***用例之间，一个用例简单地包含其他用例具有的行为
  - 包含关系把几个用例的**公共部分**分离成一个单独的被包含用例；一个用例的功能太多，用包含关系建模成两个以上的用例，**降低用例的复杂度**
  - 被包含用例称为**提供者用例**，包含用例称为**客户用例**
  - ***客户用例执行，则提供者用例必须执行***
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223142907237.png" alt="image-20211223142907237" style="zoom:50%;" />
- ***扩展关系：***基础用例的增量扩展
  - 把新的行为加到已有的用例中去
  - 基础用例提供**扩展点**以添加新的行为，扩展用例插入到基础用例的扩展点上
  - ***基础用例被执行，一般不会涉及扩展用例；只有特定的条件发生，扩展用例才被执行***，与包含关系区分
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223143320145.png" alt="image-20211223143320145" style="zoom:50%;" />
- ***泛化关系：***一般与特殊的关系
  - 父用例可以被特别地列举为一个或多个子用例，子用例表示父用例的特殊形式
  - 子用例从父用例处继承行为和属性，还可以添加行为或覆盖、改变继承的行为
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223143559930.png" alt="image-20211223143559930" style="zoom:50%;" />

### 5. 实例：图书馆管理系统的用例图（看PPT）

- ***确定系统涉及的总体信息***

- ***确定系统的参与者***

- ***确定系统的用例***（包括不同参与者的不同用例）

- ***图书馆管理系统的用例图***

### 6. 边界

- 正确用例图
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223144315863.png" alt="image-20211223144315863" style="zoom: 67%;" />
- 错误用例图
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223144342090.png" alt="image-20211223144342090" style="zoom: 67%;" />



<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223144452473.png" alt="image-20211223144452473" style="zoom: 67%;" />

### 7. 用例的粒度

是用例吗？常有**把步骤当作用例的错误**：

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223144715314.png" alt="image-20211223144715314" style="zoom:67%;" />

用例能多能少

### 8. 用例的层次

？？？？？《include》关系

### 9. 业务建模

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223145114938.png" alt="image-20211223145114938" style="zoom:80%;" />

## 三. 活动图

### 1. 活动图简介

活动图是UML用于***系统动态行为模型***工具

描述活动顺序，***<u>从一个活动到另一个活动的控制流</u>***

本质上是流程图

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223145831401.png" alt="image-20211223145831401" style="zoom:80%;" />

### 2. 活动图元素

- ***动作状态：***原子的、瞬时的、不可分解、不可中断
  - 可以有入转换（动作流、对象流），至少一条出转换
  - 不能有入口动作和出口动作，更不能有内部转移
- ***活动状态：***非原子、可分解（分解为子活动或动作状态）
  - 活动状态的**内部活动**可以用**另一个活动图**来表示
  - 活动状态可以有入口动作和出口动作，也可以有内部转移



**动作状态是活动状态的一个特例，如果某个活动状态只包括一个动作，那么它就是一个动作状态**

动作状态图和活动状态图都用平滑的圆角矩形表示

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223150943098.png" alt="image-20211223150943098" style="zoom:50%;" /><img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223150950213.png" alt="image-20211223150950213" style="zoom:50%;" />



- ***开始点***
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223151243264.png" alt="image-20211223151243264" style="zoom: 67%;" />
- ***结束点***
  - 整个活动结束
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223151255057.png" alt="image-20211223151255057" style="zoom:67%;" />
  - 子流程的结束
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223151302524.png" alt="image-20211223151302524" style="zoom:67%;" />
- ***分支与合并***
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223151329402.png" alt="image-20211223151329402" style="zoom: 67%;" />
- ***分叉与汇合***
  - 分叉用将控制流分为**两个或者多个并发运行**的分支
  - 汇合用于**同步**这些并发分支，以达到**共同完成一项事务**的目的
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223151447513.png" alt="image-20211223151447513" style="zoom:80%;" />
- ***泳道***
- ***对象流***
  - 对象放在活动图中，并用一个依赖将其连接到进行创建、修改或撤销等动作状态或者活动状态上
  - 对象流是***动作状态或者活动状态与对象之间的依赖关系***，表示动作使用对象或动作对对象的影响

### 3. 图书馆活动图

### 4. 活动图和状态图区别

- 活动图着重表现从**一个活动到另一个活动的控制流**，是***内部处理驱动的流程***

- 状态图着重描述从**一个状态到另一个状态的流程**，主要***有外部事件的参与***

### 5. 活动图和流程图区别

- 流程图着重描述处理过程，它的主要控制结构是顺序、分支和循环，各个处理之间有严格的顺序和时间关系

- 活动图描述的则是对象活动的顺序关系所遵循的规则，它着重表现的是系统的行为，而非系统的处理过程

- 活动图能够表示***并发活动***的情形，流程图不能

## 四. 类图/对象图

### 1. 类图的概念

- 描述**类、接口及它们之间关系**的图

- 显示系统中各个类的**静态结构**

### 2. 类图的元素

***类（class）、接口（interface）、依赖关系（dependency）、泛化关系（generalization）、关联关系（association）、实现关系（realization）***

### 3. 类

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/F3DFFE17429007C9A725FF957673FCF2.png" alt="img" style="zoom: 45%;" />

- ***分析阶段的类***：不考虑方法
- ***设计阶段的类***：进行拆分
- 数量对比：设计阶段类图类的数量 $\ge$ 分析阶段类数



类面向对象系统组织结构的核心

***<u>类的组成：</u>***

- ***名称（Name）：***名词、首字母大写、简单名和路径名
- ***属性（Attribute）：*** 描述对象具备的特性
  - 任意数目的属性，也可以没有属性
  - **UML类属性语法：[可见性] 属性名 [类型] [=初始值]**
    - 属性提倡私有，通过方法进行修改
    - 属性的可见性 $\left\{ \begin{aligned} public + \\ private- \\ protected\# \\ package \sim \end{aligned} \right.$
- ***操作（Operation）：*** 对类的对象所能做的事务的抽象
  - **类操作的语法为：[可见性] 操作名 [(参数列表)] [:返回类型]**
  - **返回类型、名称和参数一起被称为操作签名**

### 4. 接口

没有给出对象的实现和状态的情况下对对象行为的描述

包含操作但**不包含属性**，没有对外界可见的关联，一个类可以实现一个或多个接口

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223183017010.png" alt="image-20211223183017010" style="zoom:80%;" />

### 5. 类之间的关系

- <u>***依赖关系***</u>
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223183209032.png" alt="image-20211223183209032" style="zoom:50%;" />
  - 依赖关系的分类：**使用依赖、抽象依赖、授权依赖、绑定依赖**
    - 使用依赖，包括：调用call、参数parameter、发送send、实例化instantiate
    - 抽象依赖，包括：跟踪trace、精化refine、派生derive
    - 授权依赖，包括：访问access、导入import、友元friend
    - 绑定依赖，包括：绑定bind

- <u>***泛化关系***</u>
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223215841906.png" alt="image-20211223215841906" style="zoom:50%;" />
  - 存在于一般元素和特殊元素间的分类关系
  - 描述了一种”a kind of“的关系

- <u>***关联关系***</u>

  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223220010992.png" alt="image-20211223220010992" style="zoom:50%;" />

  - 结构关系，指明对象之间的联系
  - ***关联的名称***：动词或动词短语（不必要），指示符消除歧义
  - ***关联的角色***：动词或动词短语，关联关系中一个类对另一个类所表现出来的职责（如，学习者和教学者）
  - ***关联的多重性***：多少对象参与该关联，一个取值范围、特定值、无限定的范围或一组离散值

- <u>***实现关系***</u>
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223221006856.png" alt="image-20211223221006856" style="zoom:67%;" />
  - 接口和其实现之间的关系
- ***<u>聚合关系</u>***
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223220743091.png" alt="image-20211223220743091" style="zoom:50%;" />
  - 整体与部分的关系
- ***<u>组合</u>***
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223220816880.png" alt="image-20211223220816880" style="zoom:50%;" />
  - 强聚合，类似于人体和躯干、四肢的关系

### 6. 分析阶段的类图

分析阶段主要对领域建模，与实现技术和平台无关，只需要掌握：***类（属性、操作、可见性）***、***关联关系***、***组合关系***

使用”***事务模式***“对领域建模

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223221521392.png" alt="image-20211223221521392" style="zoom:80%;" />

### 7. 设计阶段的类图

### 8. 实例：图书馆管理系统的类图

## 五. 交互图（时序图）

### 1. 什么是交互图

交互图是描述系统中**对象之间**通过**消息通信**的图，包括：**序列图（也称时序图、顺序图）、协作图（也称通信图）**

### 2. 序列图简介

序列图用来描述系统中***对象间通过消息进行交互***，它强调消息在***时间轴上的先后***顺序。

序列图常用来描述**用例的实现**，标识了消息发生交互的**先后顺序**，明确**类的职责**

### 3. 序列图的组成

***组成元素：对象、生命线、消息、激活***

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223222353424.png" alt="image-20211223222353424" style="zoom:80%;" />



- ***对象***
  - 序列图顶部——交互开始就被创建，不在顶部——交互过程中被创建
    - 创建的两种表示
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223222948287.png" alt="image-20211223222948287" style="zoom:67%;" />
  - 名称（对象名：类名）<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223223201098.png" alt="image-20211223223201098" style="zoom:50%;" />
  - 注销：”X“符号
- ***生命线***
  - 生命线是一条**垂直的虚线**，表示序列图中的对象在**一段时间内的存在**
  - 有的生命线从顶部延伸至底部，所用的时间取决于交互持续的时间
- ***消息***
  - **对象之间某种形式的通信**
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223223346222.png" alt="image-20211223223346222" style="zoom: 67%;" />
  - 如上图所示，消息的类型：调用call（对象之间或对象本身，格式”对象名.成员方法“）、返回return（被调用对象向调用者返回一个值）、发送send（向对象发送一个信号，调用是同步的机制，而信号是一种异步的机制）、创建create和注销destroy
  - 消息的编号，顺序编号和嵌套编号
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223224217547.png" alt="image-20211223224217547" style="zoom:80%;" />
- ***激活***
  - 激活（activation）表示对象被占用以完成某个任务
  - 去激活（Deactivation）指对象处于空闲状态、等待消息
  - **矩形称为激活条或控制期，对象在激活条的顶部被激活，在完成自己的工作后被去激活**

### 4. 用例图、类图、序列图之间的关系

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223224654959.png" alt="image-20211223224654959" style="zoom:67%;" />

***<u>三种UML图对比</u>***

|               用例图               |                类图                |               序列图               |
| :--------------------------------: | :--------------------------------: | :--------------------------------: |
| **动态行为**  **（系统外在行为）** | **静态结构**  **（系统内在结构）** | **动态行为**  **（系统内在行为）** |
|          **参与者、用例**          |               **类**               |              **对象**              |
|        **包含、扩展、泛化**        |        **依赖、关联、泛化**        |              **消息**              |
|            **用例描述**            |            **事务模式**            |            **BCE模式**             |
|            **业务流程**            |            **领域概念**            |        **概念与流程的关联**        |



画图顺序：用例图 $\Rightarrow$ 类图 $\Rightarrow$ 序列图

### 5. BCE模式？？？？？

BCE（Boundary、Control、Entity）

- 边界类 Boundary：**隔离系统内部和外部**
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223225152576.png" alt="image-20211223225152576" style="zoom:50%;" />
- 控制类 Control：**在分析阶段，通常针对一个用例生成一个控制类**
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223225222108.png" alt="image-20211223225222108" style="zoom:67%;" />
- 实体类 Entity：**对应于类图中领域概念中的类**，封装数据结构和数据存储有关的类
  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223225236236.png" alt="image-20211223225236236" style="zoom:67%;" />

**新版序列图，一个序列图可以描述多个场景** $\Rightarrow$ 组合片段？（不建议）

### 6. 实例：图书馆管理系统的序列图

### 7. Frame

![image-20211223233309370](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211223233309370.png)

### 8. 组合片段

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224001943167.png" alt="image-20211224001943167" style="zoom:80%;" />



- opt：可能发生或可能不发生的序列，可以在临界条件中指定序列发生的条件
- alt：设置一个临界条件来指示该片段可以运行的条件
- loop：片段重复一定次数，可以在临界条件中指示片段重复的条件
- break：如果执行此片段，则放弃序列的其余部分
- par：并行处理
- critical：此片段中的消息不得与其他消息交错
- ref：在一个交互图中，引用其他的交互图

### 9. 协作图

***协作图***：也称为通信图，它描述了系统中，对象间通过消息进行的交互，强调了**对象在交互行为中承担的角色**

包含元素：对象、链、消息



<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224104733984.png" alt="image-20211224104733984" style="zoom:80%;" />



序列图与协作图都表示对象之间的交互作用，只是它们的侧重点有所不同

- 序列图描述了交互过程中的**时间顺序**，但没有明确地表达对象之间的关系
- 协作图**描述了对象之间的关系**，但时间顺序必须从**顺序号**获得
- 两种图的语义是等价的，可以从一种形式的图转换成另一种形式的图，而不丢失任何信息（***协作图是序列图去掉时序用序列号表示***）

## 六. 状态图

***<u>状态图</u>***主要用于描述***一个对象在其生存期间的动态行为***，表现为一个对象所经历的***状态序列***，引起状态转移的***事件***（Event），以及因状态转移而***伴随的动作***（Action）



***<u>状态图元素</u>***

- ***状态***

  - 在此期间，满足某些条件、执行某些活动或等待某些事件
  - 状态图圆角矩形表示
  - 初始状态、终止状态：<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224105746874.png" alt="image-20211224105746874" style="zoom:50%;" />

- ***<u>转移</u>***（两个状态之间的一种关系）：在**源状态**中执行一定的动作，并在某个**特定事件发生**而且某个特定的**警界条件满足**时进入目标状态

  - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224105844073.png" alt="image-20211224105844073" style="zoom:50%;" />
  - 触发事件（转移诱因）、警戒条件（条件满足才转移）、结果（对象转移后的结果）
  - 自身转移

- ***动作：***可执行的原子操作，不可中断，执行时间可忽略（EntryActions、DoActions、ExitActions）

- ***组合状态：***嵌套子状态

  - | ![image-20211224111828624](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224111828624.png) | ![image-20211224111836676](https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224111836676.png) |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |

  - 进入节点：**直接通过一个节点进入状态**，**此节点称之为进入节点或选择节点**
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224112608193.png" alt="image-20211224112608193" style="zoom:50%;" />
  - 退出节点：状态内部子状态转移到外部状态，边界经过退出节点
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224112659874.png" alt="image-20211224112659874" style="zoom:67%;" />
  - 历史状态：记住退出时的子状态
  - 并发：组合状态在某一时刻同时达到多个子状态
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224112553688.png" alt="image-20211224112553688" style="zoom:67%;" />



***<u>状态图实例</u>***

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224112742700.png" alt="image-20211224112742700" style="zoom:67%;" />

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224112802114.png" alt="image-20211224112802114" style="zoom:67%;" />

## 七. 组件图+部署图（略）

### 1. 组件图

**组件图描述了软件的各种组件以及它们之间的依赖关系**

**组件图可以用来显示编译、链接或执行时组件之间的依赖关系，以及组件的接口和调用关系**

组件图包含元素：组件、接口、依赖关系



一般组件就是一个实际文件：**deployment componen**，如dll文件、exe文件、COM+对象、CORBA对象、EJB、动态Web页、数据库表等；**work product component**，如源代码文件，数据文件等，这些构件可以用来产生deployment component；**execution component**，系统执行后得到的构件



<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224114411401.png" alt="image-20211224114411401" style="zoom:80%;" />

组件和接口之间的关系：

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224114649615.png" alt="image-20211224114649615" style="zoom:67%;" />

<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224114523592.png" alt="image-20211224114523592"  />

### 2. 部署图（实施图）

部署模型通常与组件模型并行开发



用来描述系统**硬件的物理拓扑结构**以及在此结构上执行的**软构件**

一个系统模型只有一个部署图，可以显示计算节点的拓扑结构和通信路径、节点上运行的软构件等，由体系结构设计师 / 网络工程师 / 系统工程师等描述



基本概念：node节点（处理器、设备），connection连接

- 节点是存在于运行时并代表一项计算资源的物理元素，一般至少拥有一些内存，而且通常具有处理能力
  - 处理器具有处理能力的节点，即它可以执行构件
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224120600435.png" alt="image-20211224120600435" style="zoom:80%;" />
  - 设备是无计算能力的外部设备，如Modem、终端
    - <img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224120620298.png" alt="image-20211224120620298" style="zoom:80%;" />
- 连接是代表一种交流的机制（物理媒介和软件协议）



<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224120806152.png" alt="image-20211224120806152" style="zoom:80%;" />



<img src="https://gitee.com/ifu18/blog-image/raw/master/2022/image-20211224120819802.png" alt="image-20211224120819802" style="zoom:80%;" />