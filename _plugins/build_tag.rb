# build tag文件夹
module Jekyll
	class TagIndex < Page
		def initialize(site, base, dir, tag)
			@site = site
			@base = base
			@dir = dir
			@name = 'index.html'
			self.process(@name)
			self.read_yaml(File.join(base, '_layouts'), 'tagpage.html')
			 # _layouts和tagpage.html即是我们的tagpage template所在了
			self.data['tag'] = tag
			tag_title_prefix = site.config['tag_title_prefix'] || 'Posts Tagged &ldquo;'
			tag_title_suffix = site.config['tag_title_suffix'] || '&rdquo;'
			 # 写在单页里面title域的部分
			self.data['title'] = "#{tag_title_prefix}#{tag}#{tag_title_suffix}"
		end
	end
	class TagGenerator < Generator
		safe true
		def generate(site)
			if site.layouts.key? 'tagpage'
			# 如果你用的模板名称不是"tagpage.html"的话, 记得修改这里的名字
				dir = site.config['tag_dir'] || 'tag'
				# 如果你想要自己定义tag单页存储的路径, 或者说是访问路径中的tag前缀, 可以在config里面设定 tag_dir 的值, 或者是直接改这里也行~
				site.tags.keys.each do |tag|
					write_tag_index(site, File.join(dir, tag), tag)
				end
			end
		end
		def write_tag_index(site, dir, tag)
			index = TagIndex.new(site, site.source, dir, tag)
			index.render(site.layouts, site.site_payload)
			index.write(site.dest)
			site.pages << index
		end
	end

end