---
permalink: /
title: "Liu Xiaoyu (刘晓煜)"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
/* 页面整体风格 - 暖白网格纸背景 */
body {
  background-color: #f7f5f1;
  background-image:
    linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px);
  background-size: 52px 52px;
}

.home-container {
  max-width: 1180px;
  margin: 0 auto;
  padding: 60px 20px;
}

.intro {
  text-align: center;
  margin-bottom: 60px;
  font-size: 17px;
  line-height: 1.8;
  color: #444;
}

.intro a {
  text-decoration: none;
  color: #3564ff;
  border-bottom: 1px solid #3564ff;
}

.intro strong {
  color: #111;
}

/* 板块标题 - 手写体风格 */
.section-title {
  font-family: "Brush Script MT", "Segoe Script", "Segoe UI Script", cursive;
  font-size: 48px;
  font-weight: 600;
  color: #111;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #ddd7cf;
}

/* 三列布局 */
.edu-list, .exp-list {
  display: flex;
  flex-direction: column;
}

.edu-item, .exp-item {
  display: grid;
  grid-template-columns: 140px 260px 1fr;
  column-gap: 28px;
  padding: 28px 0;
  border-bottom: 1px solid #ddd7cf;
  align-items: center;
}

/* 时间列 - monospace打字机风格 */
.edu-time, .exp-time {
  font-family: "Courier New", "Cambria Math", monospace;
  font-size: 17px;
  color: #9da3ab;
  line-height: 1.55;
  text-align: left;
}

.edu-time span, .exp-time span {
  display: block;
}

/* Logo列 */
.edu-logo img, .exp-logo img {
  max-width: 240px;
  max-height: 85px;
  object-fit: contain;
}

/* 右侧文本 - 三行样式 */
.edu-content h3, .exp-content h3 {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 21px;
  font-weight: 700;
  color: #3564ff;
  margin: 0 0 8px 0;
}

.edu-content .item-subtitle, .exp-content .item-subtitle {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 17px;
  color: #3564ff;
  margin: 0 0 6px 0;
}

.edu-content .item-desc, .exp-content .item-desc {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 17px;
  color: #7c6d5f;
  font-style: italic;
  margin: 0;
}

.exp-content ul {
  margin: 12px 0 0 0;
  padding-left: 18px;
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 16px;
  color: #555;
  line-height: 1.6;
}

.exp-content li {
  margin-bottom: 6px;
}

/* 科研项目卡片 */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 25px;
}

.project-card {
  border: 1px solid #ddd7cf;
  border-radius: 6px;
  padding: 22px;
  background: rgba(255,255,255,0.5);
}

.project-card h3 {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 18px;
  font-weight: 700;
  color: #3564ff;
  margin: 0 0 8px 0;
}

.project-card .project-meta {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 14px;
  color: #888;
  margin-bottom: 12px;
}

.project-card .project-desc {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 15px;
  color: #555;
  line-height: 1.6;
}

.project-card .project-desc ul {
  margin: 8px 0;
  padding-left: 16px;
}

.project-card .project-desc li {
  margin-bottom: 4px;
}

/* 论文列表 */
.pub-list {
  list-style: none;
  padding: 0;
  font-family: "Cambria Math", "Times New Roman", serif;
}

.pub-list li {
  margin-bottom: 18px;
  padding-bottom: 18px;
  border-bottom: 1px solid #eee;
  font-size: 16px;
  color: #555;
}

.pub-list li:last-child {
  border-bottom: none;
}

.pub-list li strong {
  color: #111;
}

/* 技能网格 */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
}

.skill-item {
  background: rgba(255,255,255,0.6);
  padding: 14px 16px;
  border-radius: 4px;
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 15px;
  color: #444;
  border: 1px solid #e8e4dc;
}

/* Section spacing */
.section {
  margin: 70px 0;
}

/* 中文页面字体 */
:lang(zh) .home-container,
:lang(zh) body {
  font-family: "微软雅黑", "Microsoft YaHei", "宋体", "SimSun", serif;
}

:lang(zh) .edu-content h3,
:lang(zh) .exp-content h3,
:lang(zh) .edu-content .item-subtitle,
:lang(zh) .exp-content .item-subtitle,
:lang(zh) .edu-content .item-desc,
:lang(zh) .exp-content .item-desc,
:lang(zh) .exp-content ul,
:lang(zh) .exp-content li,
:lang(zh) .project-card h3,
:lang(zh) .project-card .project-meta,
:lang(zh) .project-card .project-desc,
:lang(zh) .project-card .project-desc li,
:lang(zh) .pub-list li,
:lang(zh) .skill-item {
  font-family: "微软雅黑", "Microsoft YaHei", "宋体", "SimSun", serif;
}

:lang(zh) .section-title {
  font-family: "微软雅黑", "Microsoft YaHei", "黑体", serif;
  font-size: 36px;
}
</style>

<!-- 英文版 -->
<div id="lang-en" class="home-container">
  <div class="intro">
    I am an incoming M.S. student in <strong>Electronic Information</strong> at <a href="https://www.buaa.edu.cn/">Beihang University</a> (Sept 2026, direct admission). I received my B.E. in <strong>Measurement & Control Technology and Instrumentation</strong> from <a href="https://www.whut.edu.cn/">Wuhan University of Technology</a> in 2026.<br><br>
    My interests lie at the intersection of <strong>autonomous robotics</strong>, <strong>embedded systems</strong>, and <strong>intelligent perception</strong>. I enjoy turning research ideas into working hardware and software.<br><br>
    <a href="mailto:339300@whut.edu.cn">339300@whut.edu.cn</a>
  </div>

  <div class="section">
    <h2 class="section-title">Education</h2>
    <div class="edu-list">
      <div class="edu-item">
        <div class="edu-time">
          <span>Sep. 2026</span>
          <span>—</span>
          <span>Jun. 2029</span>
        </div>
        <div class="edu-logo">
          <img src="/images/lxy/school/buaa.png" alt="Beihang University">
        </div>
        <div class="edu-content">
          <h3>Beihang University (BUAA)</h3>
          <p class="item-subtitle">School of Automation Science and Electrical Engineering</p>
          <p class="item-desc">M.S. in Electronic Information · Direct admission</p>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-time">
          <span>Sep. 2022</span>
          <span>—</span>
          <span>Jun. 2026</span>
        </div>
        <div class="edu-logo">
          <img src="/images/lxy/school/wut.png" alt="Wuhan University of Technology">
        </div>
        <div class="edu-content">
          <h3>Wuhan University of Technology</h3>
          <p class="item-subtitle">School of Mechanical and Electronic Engineering</p>
          <p class="item-desc">B.E. in Measurement & Control Technology and Instrumentation</p>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">Internship</h2>
    <div class="exp-list">
      <div class="exp-item">
        <div class="exp-time">
          <span>Nov. 2025</span>
          <span>—</span>
          <span>Mar. 2026</span>
        </div>
        <div class="exp-logo">
          <img src="/images/lxy/school/momenta.png" alt="Momenta">
        </div>
        <div class="exp-content">
          <h3>Momenta</h3>
          <p class="item-subtitle">System Integration Architecture Intern · Beijing / Remote</p>
          <ul>
            <li>Responsible for OTA3 integration, release, and delivery for Dongfeng Nissan N7 intelligent driving software.</li>
            <li>Contributed to CPU/memory optimization across Nissan N6/N7/N8 platforms (QC8778, Orin-N, Orin-Y).</li>
            <li>Built automation pipelines and a Feishu bot using Claude Code.</li>
          </ul>
        </div>
      </div>
      <div class="exp-item">
        <div class="exp-time">
          <span>Jun. 2025</span>
          <span>—</span>
          <span>Aug. 2025</span>
        </div>
        <div class="exp-logo">
          <img src="/images/lxy/school/zju.png" alt="ZJU Huzhou">
        </div>
        <div class="exp-content">
          <h3>Zhejiang University Huzhou Research Institute</h3>
          <p class="item-subtitle">Robot Navigation Algorithm Intern · Huzhou</p>
          <ul>
            <li>Researched autonomous navigation for small carrier vehicles in GNSS-denied environments.</li>
            <li>Designed an Ackermann-chassis local planner based on RRP pure-pursuit algorithm.</li>
            <li>Assisted in assembling 6 robot prototypes; wrote middleware and analyzed sensor data.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">Research Projects</h2>
    <div class="project-grid">
      <div class="project-card">
        <h3>Bionic Octopus Venlo Roof Cleaning Robot</h3>
        <p class="project-meta">National Innovation Project (2024–2025) · National Excellent</p>
        <div class="project-desc">
          <ul>
            <li>Led a team to design a wall-climbing robot for 20°–35° Venlo greenhouse roofs.</li>
            <li>Developed negative-pressure adhesion model, kinematic simulation, three motion modes on STM32, and perception/navigation system on Horizon RDK X5.</li>
            <li>Outcome: 1 EI paper, 1 invention patent, selected for 18th National Student Innovation Conference.</li>
          </ul>
        </div>
      </div>
      <div class="project-card">
        <h3>AGV Stacking Robot</h3>
        <p class="project-meta">China Robot Competition 2024 · National 3rd Prize</p>
        <div class="project-desc">
          <ul>
            <li>Designed stereoscopic-warehouse AGV with vision-based autonomous decision-making (OpenCV).</li>
            <li>Developed closed-loop localization system fusing gyroscope, photoelectric, and ultrasonic sensors.</li>
          </ul>
        </div>
      </div>
      <div class="project-card">
        <h3>Soft-Rock Drilling & Pipe-Laying Robot</h3>
        <p class="project-meta">CSMEE Innovation Competition 2024 · National 1st Prize</p>
        <div class="project-desc">
          <ul>
            <li>Designed three-stage planetary gear torque regulator, spring-impact structure, ball-spring torque limiter.</li>
            <li>Full mechanical modeling, stress simulation, animation rendering in Inventor / Fusion360 / Blender.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">Publications & Patents</h2>
    <ul class="pub-list">
      <li><strong>X. Liu</strong>, "Design of Venlo-type Greenhouse Roof Cleaning Robot," <em>ICMIII 2025</em> (EI indexed). [May 2025]</li>
      <li>Zhang Jinguang, <strong>Liu Xiaoyu</strong>, et al. <em>A Roof Cleaning Robot.</em> Invention patent, Application No. 202510500482.5. [Apr 2025]</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="section-title">Skills</h2>
    <div class="skills-grid">
      <div class="skill-item"><strong>Robotics:</strong> ROS (C++), SLAM, navigation</div>
      <div class="skill-item"><strong>Software:</strong> Python, Shell, Linux, Git, Qt/C++</div>
      <div class="skill-item"><strong>Embedded:</strong> STM32, C51, hardware-in-loop</div>
      <div class="skill-item"><strong>Mechanical:</strong> Inventor, Fusion360, Blender</div>
      <div class="skill-item"><strong>Vision:</strong> OpenCV</div>
      <div class="skill-item"><strong>Photography:</strong> Published in China Daily (2023)</div>
    </div>
  </div>
</div>

<!-- 中文版 -->
<div id="lang-zh" class="home-container" style="display: none;">
  <div class="intro">
    我是<strong>北京航空航天大学</strong>电子信息专业2026年9月入学的硕士研究生（直接推免）。我于2026年从<strong>武汉理工大学</strong>获得<strong>测控技术与仪器</strong>专业学士学位。<br><br>
    我的研究兴趣集中在<strong>自主机器人</strong>、<strong>嵌入式系统</strong>和<strong>智能感知</strong>的交叉领域。我热衷于将研究想法转化为实际可用的硬件和软件。<br><br>
    <a href="mailto:339300@whut.edu.cn">339300@whut.edu.cn</a>
  </div>

  <div class="section">
    <h2 class="section-title">教育背景</h2>
    <div class="edu-list">
      <div class="edu-item">
        <div class="edu-time">
          <span>2026.9</span>
          <span>—</span>
          <span>2029.6</span>
        </div>
        <div class="edu-logo">
          <img src="/images/lxy/school/buaa.png" alt="北京航空航天大学">
        </div>
        <div class="edu-content">
          <h3>北京航空航天大学</h3>
          <p class="item-subtitle">自动化科学与电气工程学院</p>
          <p class="item-desc">电子信息硕士研究生 · 直接推免</p>
        </div>
      </div>
      <div class="edu-item">
        <div class="edu-time">
          <span>2022.9</span>
          <span>—</span>
          <span>2026.6</span>
        </div>
        <div class="edu-logo">
          <img src="/images/lxy/school/wut.png" alt="武汉理工大学">
        </div>
        <div class="edu-content">
          <h3>武汉理工大学</h3>
          <p class="item-subtitle">机电工程学院</p>
          <p class="item-desc">测控技术与仪器专业学士</p>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">实习经历</h2>
    <div class="exp-list">
      <div class="exp-item">
        <div class="exp-time">
          <span>2025.11</span>
          <span>—</span>
          <span>2026.3</span>
        </div>
        <div class="exp-logo">
          <img src="/images/lxy/school/momenta.png" alt="Momenta">
        </div>
        <div class="exp-content">
          <h3>Momenta (魔门塔)</h3>
          <p class="item-subtitle">系统集成架构实习生 · 北京 / 远程</p>
          <ul>
            <li>负责东风日产N7智能驾驶软件的OTA3集成、发布与交付。</li>
            <li>参与日产N6/N7/N8平台CPU/内存资源优化。</li>
            <li>使用Claude Code构建自动化流水线和飞书机器人。</li>
          </ul>
        </div>
      </div>
      <div class="exp-item">
        <div class="exp-time">
          <span>2025.6</span>
          <span>—</span>
          <span>2025.8</span>
        </div>
        <div class="exp-logo">
          <img src="/images/lxy/school/zju.png" alt="浙江大学">
        </div>
        <div class="exp-content">
          <h3>浙江大学湖州研究院</h3>
          <p class="item-subtitle">机器人导航算法实习生 · 湖州</p>
          <ul>
            <li>研究GNSS拒止环境下小型载具的自主导航与控制。</li>
            <li>设计基于RRP纯追踪算法的阿克曼底盘局部规划器。</li>
            <li>协助组装6台机器人样机，编写中间件并分析传感器数据。</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">科研项目</h2>
    <div class="project-grid">
      <div class="project-card">
        <h3>仿生章鱼文洛型温室屋顶清洁机器人</h3>
        <p class="project-meta">国家大学生创新项目 (2024–2025) · 国家优秀</p>
        <div class="project-desc">
          <ul>
            <li>带领团队设计适用于20°–35°文洛型温室屋顶的爬壁机器人。</li>
            <li>研发负压吸附模型、运动学仿真、STM32三种运动模式及RDK X5感知导航系统。</li>
            <li>成果：1篇EI论文、1项发明专利、入选第18届全国大学生创新年会。</li>
          </ul>
        </div>
      </div>
      <div class="project-card">
        <h3>AGV码垛机器人</h3>
        <p class="project-meta">中国机器人竞赛 2024 · 国家三等奖</p>
        <div class="project-desc">
          <ul>
            <li>设计基于视觉自主决策的立体仓库AGV。</li>
            <li>开发融合陀螺仪，光电和超声波传感器的轮式里程计闭环定位系统。</li>
          </ul>
        </div>
      </div>
      <div class="project-card">
        <h3>软岩钻孔铺管机器人</h3>
        <p class="project-meta">全国机械创新设计大赛 2024 · 国家一等奖</p>
        <div class="project-desc">
          <ul>
            <li>设计三段式行星齿轮扭矩调节器、弹簧冲击结构、球簧扭矩限制器。</li>
            <li>在Inventor/Fusion360/Blender中完成机械建模与仿真。</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">论文与专利</h2>
    <ul class="pub-list">
      <li><strong>刘晓煜</strong>，\"Design of Venlo-type Greenhouse Roof Cleaning Robot,\" <em>ICMIII 2025</em> (EI indexed). [2025年5月]</li>
      <li>张金光、<strong>刘晓煜</strong> 等。 <em>一种屋顶清洁机器人。</em> 发明专利，申请号：202510500482.5。 [2025年4月]</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="section-title">技能</h2>
    <div class="skills-grid">
      <div class="skill-item"><strong>机器人：</strong>ROS (C++)、SLAM、导航</div>
      <div class="skill-item"><strong>软件：</strong>Python、Shell、Linux、Git、Qt/C++</div>
      <div class="skill-item"><strong>嵌入式：</strong>STM32、C51、硬件在环</div>
      <div class="skill-item"><strong>机械：</strong>Inventor、Fusion360、Blender</div>
      <div class="skill-item"><strong>视觉：</strong>OpenCV</div>
      <div class="skill-item"><strong>摄影：</strong>作品发表于《中国日报》(2023)</div>
    </div>
  </div>
</div>

<script>
// 默认语言为中文
(function() {
  var enDiv = document.getElementById('lang-en');
  var zhDiv = document.getElementById('lang-zh');

  function setLanguage(lang) {
    if (lang === 'zh') {
      enDiv.style.display = 'none';
      zhDiv.style.display = 'block';
      document.documentElement.lang = 'zh';
    } else {
      enDiv.style.display = 'block';
      zhDiv.style.display = 'none';
      document.documentElement.lang = 'en';
    }
  }

  // 默认设置为中文
  localStorage.setItem('lang', 'zh');
  setLanguage('zh');

  window.addEventListener('languageChange', function(e) {
    setLanguage(e.detail.lang);
  });
})();
</script>
