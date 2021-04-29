require 'thread'
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

class ColorFlags

  def initialize(graph)
    @colors_palette = {0=>"R", 1=>"H", 2=>"B", 3=>"G", 4=>"O", 6=>"L", 7=>"P"}
    
    @result = Array.new(graph.v)

    
    bfs(graph, s)
  end

  def bfs(graph)
    @result = 0
      (0..graph.v).each do |v|
        @result[v] = -1
      end    

      (0..graph.v).each do |v|
        @available[v] = false
      end    

      (0...graph.v).each do |u|
        (graph.get_adj(u)).each do |i|
          if result[i] != -1
             available[result[i]] = true       
          end

          cr=-1
          (0..graph.v).each_with_index  do |e,index|
            if available[index] == false
              cr=index
              break
            end
          end

          result[u] =cr

          for 
      end

  end

  def get_market(w)
    @marked[w]
  end
end

g = Graph.new(13)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(0,4)
g.add_edge(0,5)

g.add_edge(1,2)
g.add_edge(1,6)
g.add_edge(2,3)
g.add_edge(2,6)


g.add_edge(3,4)
g.add_edge(3,8)
g.add_edge(3,6)
g.add_edge(3,7)
g.add_edge(3,9)
g.add_edge(3,10)

g.add_edge(4,5)
g.add_edge(4,9)
g.add_edge(4,10)

g.add_edge(5,10)

g.add_edge(6,7)

g.add_edge(8,10)

g.add_edge(9,10)

g.add_edge(11,12)


countries = { 0 => "PERU", 1=>"ECUADOR", 2=>"COLOMBIA", 3=>"BRASIL", 4=>"BOLIVIA", 5=>"CHILE", 6=>"VENEZUELA", 7=>"GUYANA", 8=>"URUGUAY", 9=>"PARAGUAY", 10=>"ARGENTINA", 11=>"MEXICO", 12=>"USA"}
colors = {0=>"R", 1=>"H", 2=>"B", 3=>"G", 4=>"O", 6=>"L", 7=>"P"}

search=ColorFlags.new(g,8)
(0..g.v).each do |v|
  if search.get_market(v)
    puts "#{countries[v]}"
    end
end
puts "\n"




