class Graph
  attr_accessor :e, :v, :adj
  def initialize(v)
		@v = v
		@e = 0
		@adj = Array.new(v) { Array.[] }
	end

  def add_edge(v, w)
    @adj[v].push(w)
    @adj[w].push(v)
    @e+=1
  end

  def get_adj(v)
     @adj[v]
  end
end

class DeepFirstSearch
  attr_accessor :count

  def initialize(graph, s)
    @count = 0
    @marked = Array.new(graph.v)
    dfs(graph, s)
  end

  def dfs(graph,v)
    @marked[v] = true
    @count += 1
    (graph.get_adj(v)).each do |w|
      if !@marked[w]
        dfs(graph, w)
      end
    end
  end

  def get_market(w)
    @marked[w]
  end
end

g = Graph.new(13)
g.add_edge(0,5)
g.add_edge(4,3)
g.add_edge(0,1)
g.add_edge(9,12)
g.add_edge(6,4)
g.add_edge(5,4)
g.add_edge(0,2)
g.add_edge(11,12)
g.add_edge(9,10)
g.add_edge(0,6)
g.add_edge(7,8)
g.add_edge(9,11)
g.add_edge(5,3)

search=DeepFirstSearch.new(g,10)
(0..g.v).each do |v|
  if search.get_market(v)
    print "#{v} "
    end
end
puts "\n"




