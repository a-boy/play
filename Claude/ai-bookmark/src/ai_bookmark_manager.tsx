import React, { useState, useEffect } from 'react';
import { Search, Bookmark, Plus, Tag, Globe, Trash2, Brain, Sparkles } from 'lucide-react';

const AIBookmarkManager = () => {
  const [bookmarks, setBookmarks] = useState([
    {
      id: 1,
      title: "ChatGPT",
      url: "https://chat.openai.com",
      description: "OpenAI's conversational AI assistant for writing, coding, analysis, and creative tasks",
      category: "AI Assistants",
      tags: ["chatbot", "openai", "gpt", "writing", "coding"],
      aiGenerated: true
    },
    {
      id: 2,
      title: "Anthropic Claude",
      url: "https://claude.ai",
      description: "Advanced AI assistant for coding, writing, analysis, and complex reasoning tasks",
      category: "AI Assistants",
      tags: ["ai", "assistant", "anthropic", "reasoning", "coding"],
      aiGenerated: true
    },
    {
      id: 3,
      title: "Midjourney",
      url: "https://midjourney.com",
      description: "AI-powered image generation tool for creating stunning artwork and visuals",
      category: "AI Image Generation",
      tags: ["image", "art", "generation", "creative", "discord"],
      aiGenerated: true
    },
    {
      id: 4,
      title: "Perplexity AI",
      url: "https://perplexity.ai",
      description: "AI-powered search engine that provides detailed answers with source citations",
      category: "AI Search",
      tags: ["search", "research", "citations", "answers", "web"],
      aiGenerated: true
    },
    {
      id: 5,
      title: "DALL-E 2",
      url: "https://openai.com/dall-e-2",
      description: "OpenAI's AI system for creating realistic images from natural language descriptions",
      category: "AI Image Generation",
      tags: ["openai", "image", "generation", "dalle", "creative"],
      aiGenerated: true
    },
    {
      id: 6,
      title: "Google Gemini",
      url: "https://gemini.google.com",
      description: "Google's multimodal AI assistant for text, code, images, and more",
      category: "AI Assistants",
      tags: ["google", "gemini", "multimodal", "assistant", "bard"],
      aiGenerated: true
    },
    {
      id: 7,
      title: "Synthesia",
      url: "https://synthesia.io",
      description: "AI video generation platform for creating professional videos with AI avatars",
      category: "AI Video",
      tags: ["video", "avatars", "generation", "presentation", "synthetic"],
      aiGenerated: true
    },
    {
      id: 8,
      title: "Stability AI",
      url: "https://stability.ai",
      description: "Open-source AI models including Stable Diffusion for image generation",
      category: "AI Platforms",
      tags: ["stable-diffusion", "open-source", "models", "image", "generation"],
      aiGenerated: true
    },
    {
      id: 9,
      title: "RunwayML",
      url: "https://runwayml.com",
      description: "AI-powered creative tools for video editing, image generation, and more",
      category: "AI Creative Tools",
      tags: ["runway", "video", "editing", "creative", "generation"],
      aiGenerated: true
    },
    {
      id: 10,
      title: "Jasper AI",
      url: "https://jasper.ai",
      description: "AI writing assistant for marketing copy, blog posts, and content creation",
      category: "AI Writing",
      tags: ["writing", "marketing", "content", "copy", "jasper"],
      aiGenerated: true
    },
    {
      id: 11,
      title: "Copy.ai",
      url: "https://copy.ai",
      description: "AI-powered copywriting tool for marketing content and creative writing",
      category: "AI Writing",
      tags: ["copywriting", "marketing", "content", "ai", "writing"],
      aiGenerated: true
    },
    {
      id: 12,
      title: "Notion AI",
      url: "https://notion.so/product/ai",
      description: "AI-powered writing and productivity features integrated into Notion workspace",
      category: "AI Productivity",
      tags: ["notion", "productivity", "writing", "workspace", "organization"],
      aiGenerated: true
    },
    {
      id: 13,
      title: "GitHub Copilot",
      url: "https://github.com/features/copilot",
      description: "AI pair programmer that helps write code faster with intelligent suggestions",
      category: "AI Coding",
      tags: ["github", "coding", "programming", "copilot", "development"],
      aiGenerated: true
    },
    {
      id: 14,
      title: "Hugging Face",
      url: "https://huggingface.co",
      description: "Platform for machine learning models, datasets, and AI community collaboration",
      category: "AI Platforms",
      tags: ["models", "datasets", "ml", "open-source", "community"],
      aiGenerated: true
    },
    {
      id: 15,
      title: "Character.AI",
      url: "https://character.ai",
      description: "Platform for creating and chatting with AI characters and personalities",
      category: "AI Entertainment",
      tags: ["characters", "roleplay", "chat", "entertainment", "personalities"],
      aiGenerated: true
    },
    {
      id: 16,
      title: "Replika",
      url: "https://replika.com",
      description: "AI companion app for meaningful conversations and emotional support",
      category: "AI Companions",
      tags: ["companion", "emotional", "support", "chat", "personal"],
      aiGenerated: true
    },
    {
      id: 17,
      title: "DeepL Translator",
      url: "https://deepl.com",
      description: "AI-powered translation service with superior accuracy and natural output",
      category: "AI Translation",
      tags: ["translation", "language", "deepl", "accurate", "multilingual"],
      aiGenerated: true
    },
    {
      id: 18,
      title: "Luma AI",
      url: "https://lumalabs.ai",
      description: "AI for 3D capture and generation from photos and text descriptions",
      category: "AI 3D Generation",
      tags: ["3d", "capture", "generation", "luma", "photogrammetry"],
      aiGenerated: true
    },
    {
      id: 19,
      title: "Futurepedia",
      url: "https://futurepedia.io",
      description: "Comprehensive directory of AI tools and software for various use cases",
      category: "AI Directories",
      tags: ["directory", "tools", "discovery", "catalog", "ai-tools"],
      aiGenerated: true
    },
    {
      id: 20,
      title: "There's An AI For That",
      url: "https://theresanaiforthat.com",
      description: "Database of AI tools categorized by use case and functionality",
      category: "AI Directories",
      tags: ["directory", "database", "tools", "search", "categories"],
      aiGenerated: true
    },
    {
      id: 21,
      title: "Eleven Labs",
      url: "https://elevenlabs.io",
      description: "AI voice generation and cloning technology for realistic speech synthesis",
      category: "AI Voice",
      tags: ["voice", "speech", "synthesis", "cloning", "audio"],
      aiGenerated: true
    },
    {
      id: 22,
      title: "Midjourney Discord",
      url: "https://discord.gg/midjourney",
      description: "Official Discord server for accessing Midjourney AI image generation",
      category: "AI Communities",
      tags: ["discord", "midjourney", "community", "image", "generation"],
      aiGenerated: true
    },
    {
      id: 23,
      title: "OpenAI Playground",
      url: "https://platform.openai.com/playground",
      description: "Interactive interface for experimenting with OpenAI's language models",
      category: "AI Development",
      tags: ["openai", "playground", "api", "development", "testing"],
      aiGenerated: true
    },
    {
      id: 24,
      title: "Poe by Quora",
      url: "https://poe.com",
      description: "Access multiple AI models including ChatGPT, Claude, and others in one platform",
      category: "AI Platforms",
      tags: ["poe", "quora", "multiple-models", "chatbots", "platform"],
      aiGenerated: true
    },
    {
      id: 25,
      title: "Bing Chat",
      url: "https://bing.com/chat",
      description: "Microsoft's AI-powered search and chat experience with web integration",
      category: "AI Search",
      tags: ["microsoft", "bing", "search", "chat", "web-integration"],
      aiGenerated: true
    }
  ]);
  
  const [newBookmark, setNewBookmark] = useState({
    title: '',
    url: '',
    description: '',
    category: '',
    tags: ''
  });
  
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [isAddingBookmark, setIsAddingBookmark] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  // Get unique categories
  const categories = ['All', ...new Set(bookmarks.map(b => b.category))];

  // Smart categorization function (simulated AI)
  const categorizeBookmark = async (url, title, description) => {
    setIsAnalyzing(true);
    
    // Simulate AI analysis
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    const keywords = (title + ' ' + description).toLowerCase();
    
    let category = 'General';
    let suggestedTags = [];
    
    if (keywords.includes('react') || keywords.includes('javascript') || keywords.includes('code') || keywords.includes('programming')) {
      category = 'Development';
      suggestedTags = ['programming', 'web development'];
    } else if (keywords.includes('ai') || keywords.includes('machine learning') || keywords.includes('artificial intelligence')) {
      category = 'AI Tools';
      suggestedTags = ['ai', 'technology'];
    } else if (keywords.includes('design') || keywords.includes('ui') || keywords.includes('ux')) {
      category = 'Design';
      suggestedTags = ['design', 'creativity'];
    } else if (keywords.includes('news') || keywords.includes('article') || keywords.includes('blog')) {
      category = 'News & Articles';
      suggestedTags = ['reading', 'information'];
    } else if (keywords.includes('tool') || keywords.includes('productivity')) {
      category = 'Productivity';
      suggestedTags = ['tools', 'productivity'];
    }
    
    // Add domain-based tags
    try {
      const domain = new URL(url).hostname.replace('www.', '');
      suggestedTags.push(domain);
    } catch (e) {
      // Invalid URL
    }
    
    setIsAnalyzing(false);
    return { category, tags: suggestedTags };
  };

  // Add bookmark with AI categorization
  const addBookmark = async () => {
    if (!newBookmark.title || !newBookmark.url) return;
    
    const aiSuggestions = await categorizeBookmark(
      newBookmark.url, 
      newBookmark.title, 
      newBookmark.description
    );
    
    const bookmark = {
      id: Date.now(),
      title: newBookmark.title,
      url: newBookmark.url,
      description: newBookmark.description || `AI-suggested: Website about ${newBookmark.title}`,
      category: newBookmark.category || aiSuggestions.category,
      tags: newBookmark.tags ? 
        newBookmark.tags.split(',').map(t => t.trim()) : 
        aiSuggestions.tags,
      aiGenerated: !newBookmark.category || !newBookmark.tags
    };
    
    setBookmarks([bookmark, ...bookmarks]);
    setNewBookmark({ title: '', url: '', description: '', category: '', tags: '' });
    setIsAddingBookmark(false);
  };

  // Smart search function
  const filteredBookmarks = bookmarks.filter(bookmark => {
    const matchesSearch = searchTerm === '' || 
      bookmark.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      bookmark.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      bookmark.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase())) ||
      bookmark.url.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesCategory = selectedCategory === 'All' || bookmark.category === selectedCategory;
    
    return matchesSearch && matchesCategory;
  });

  const deleteBookmark = (id) => {
    setBookmarks(bookmarks.filter(b => b.id !== id));
  };

  const getDomainFavicon = (url) => {
    try {
      const domain = new URL(url).hostname;
      return `https://www.google.com/s2/favicons?domain=${domain}&sz=16`;
    } catch {
      return null;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-100 p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Brain className="w-8 h-8 text-purple-600" />
            <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
              AI Smart Bookmarks
            </h1>
            <Sparkles className="w-8 h-8 text-blue-600" />
          </div>
          <p className="text-gray-600 text-lg">Intelligent bookmark management with AI-powered categorization</p>
        </div>

        {/* Search and Controls */}
        <div className="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 mb-6">
          <div className="flex flex-col md:flex-row gap-4 items-center">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
              <input
                type="text"
                placeholder="Search bookmarks by title, description, tags, or URL..."
                className="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            
            <select
              className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
            >
              {categories.map(category => (
                <option key={category} value={category}>{category}</option>
              ))}
            </select>
            
            <button
              onClick={() => setIsAddingBookmark(true)}
              className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg hover:from-purple-700 hover:to-blue-700 transition-all duration-200 shadow-lg hover:shadow-xl"
            >
              <Plus className="w-5 h-5" />
              Add Bookmark
            </button>
          </div>
        </div>

        {/* Add Bookmark Form */}
        {isAddingBookmark && (
          <div className="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-6 mb-6 border border-purple-200">
            <h3 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <Bookmark className="w-5 h-5 text-purple-600" />
              Add New Bookmark
              {isAnalyzing && (
                <div className="flex items-center gap-2 text-blue-600 text-sm">
                  <div className="animate-spin w-4 h-4 border-2 border-blue-600 border-t-transparent rounded-full"></div>
                  AI Analyzing...
                </div>
              )}
            </h3>
            
            <div className="grid md:grid-cols-2 gap-4">
              <input
                type="text"
                placeholder="Title *"
                className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                value={newBookmark.title}
                onChange={(e) => setNewBookmark({...newBookmark, title: e.target.value})}
              />
              <input
                type="url"
                placeholder="URL *"
                className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                value={newBookmark.url}
                onChange={(e) => setNewBookmark({...newBookmark, url: e.target.value})}
              />
              <input
                type="text"
                placeholder="Category (AI will suggest if empty)"
                className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                value={newBookmark.category}
                onChange={(e) => setNewBookmark({...newBookmark, category: e.target.value})}
              />
              <input
                type="text"
                placeholder="Tags (comma-separated, AI will suggest if empty)"
                className="px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                value={newBookmark.tags}
                onChange={(e) => setNewBookmark({...newBookmark, tags: e.target.value})}
              />
            </div>
            
            <textarea
              placeholder="Description (AI will generate if empty)"
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 mt-4"
              rows="3"
              value={newBookmark.description}
              onChange={(e) => setNewBookmark({...newBookmark, description: e.target.value})}
            />
            
            <div className="flex gap-3 mt-4">
              <button
                onClick={addBookmark}
                disabled={isAnalyzing || !newBookmark.title || !newBookmark.url}
                className="flex items-center gap-2 px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Brain className="w-4 h-4" />
                {isAnalyzing ? 'Processing...' : 'Add with AI'}
              </button>
              <button
                onClick={() => setIsAddingBookmark(false)}
                className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors"
              >
                Cancel
              </button>
            </div>
          </div>
        )}

        {/* Bookmarks Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredBookmarks.map(bookmark => (
            <div key={bookmark.id} className="bg-white/90 backdrop-blur-sm rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 border border-gray-100">
              <div className="flex items-start justify-between mb-3">
                <div className="flex items-center gap-2">
                  {getDomainFavicon(bookmark.url) && (
                    <img 
                      src={getDomainFavicon(bookmark.url)} 
                      alt="" 
                      className="w-4 h-4"
                      onError={(e) => e.target.style.display = 'none'}
                    />
                  )}
                  <Globe className="w-4 h-4 text-gray-400" />
                </div>
                <div className="flex gap-2">
                  {bookmark.aiGenerated && (
                    <Brain className="w-4 h-4 text-purple-500" title="AI Enhanced" />
                  )}
                  <button
                    onClick={() => deleteBookmark(bookmark.id)}
                    className="text-red-400 hover:text-red-600 transition-colors"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
              
              <h3 className="font-semibold text-lg mb-2 line-clamp-2">{bookmark.title}</h3>
              <p className="text-gray-600 text-sm mb-3 line-clamp-2">{bookmark.description}</p>
              
              <div className="flex items-center gap-2 mb-3">
                <Tag className="w-3 h-3 text-gray-400" />
                <span className="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded-full">
                  {bookmark.category}
                </span>
              </div>
              
              <div className="flex flex-wrap gap-1 mb-4">
                {bookmark.tags.map(tag => (
                  <span key={tag} className="text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-full">
                    {tag}
                  </span>
                ))}
              </div>
              
              <a
                href={bookmark.url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-purple-600 hover:text-purple-800 text-sm font-medium transition-colors"
              >
                Visit Website
                <Globe className="w-4 h-4" />
              </a>
            </div>
          ))}
        </div>

        {filteredBookmarks.length === 0 && (
          <div className="text-center py-12">
            <Bookmark className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <h3 className="text-xl text-gray-500 mb-2">No bookmarks found</h3>
            <p className="text-gray-400">Try adjusting your search or add some bookmarks to get started!</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default AIBookmarkManager;