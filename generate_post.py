#!/usr/bin/env python3
import json

with open('db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find the post
for post in data.get('Post', []):
    if post.get('slug') == 'cim-llm-inference-acceleration':
        content = post.get('content', '')
        title = post.get('title', '')

        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - 爱很简单</title>
  <meta name="description" content="本文综述了数字存算一体（CIM）技术在LLM推理加速中的最新研究进展。">
  <meta name="keywords" content="存算一体,CIM,LLM,推理加速,AI芯片">
  <link rel="canonical" href="https://CCCCCCeYes.github.io/2026/03/14/cim-llm-inference-acceleration/">
  <link rel="stylesheet" href="/css/index.css">
</head>
<body>
  <div class="wrapper">
    <header class="header">
  <nav class="navbar">
    <div class="logo">
      <a href="/">爱很简单</a>
    </div>
    <ul class="menu">
      <li><a href="/">首页</a></li>
      <li><a href="/archives/">归档</a></li>
      <li><a href="/categories/">分类</a></li>
      <li><a href="/tags/">标签</a></li>
      <li><a href="/about/">关于</a></li>
    </ul>
  </nav>
</header>

    <main class="main">
      <article class="post" itemscope itemtype="http://schema.org/BlogPosting">
  <header class="post-header">
    <h1 class="post-title" itemprop="name headline">{title}</h1>
    <div class="post-meta">
      <time datetime="{post.get('date', '').replace('Z', '')}" itemprop="datePublished">2026-03-14</time>
      <span class="author" itemprop="author">{post.get('author', 'bobo')}</span>
      <span class="category">
        <a href="/categories/%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6/">技术研究</a>
      </span>
    </div>
    <div class="post-tags">
      <a href="/tags/%E5%AD%98%E7%AE%97%E4%B8%80%E4%BD%93/">存算一体</a>
      <a href="/tags/CIM/">CIM</a>
      <a href="/tags/LLM/">LLM</a>
      <a href="/tags/%E6%8E%A8%E7%90%86%E5%8A%A0%E9%80%9F/">推理加速</a>
      <a href="/tags/AI%E8%8A%AF%E7%89%87/">AI芯片</a>
    </div>
  </header>

  <div class="post-content" itemprop="articleBody">
    {content}
  </div>

  <footer class="post-footer">
    <div class="post-copyright">
      <p>版权声明：本文为原创文章，转载请注明出处。</p>
    </div>
  </footer>
</article>

    </main>

    <footer class="footer">
  <div class="footer-content">
    <p>&copy; 2026 爱很简单. All rights reserved.</p>
  </div>
</footer>

  </div>
</body>
</html>'''

        output_path = 'public/2026/03/14/cim-llm-inference-acceleration/index.html'
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(html)
        print(f'✅ Generated {output_path}')
        break
else:
    print('❌ Post not found in db.json')
