'Alvaro Carpio 2014, All Rights Reserved .. Gagaga'
class LifeGame

 def initialize(cells)
   puts "**********INPUT**********"
   @cells = cells
   print_cells()
 end

 def run(n_times)
   (1..n_times).each do |i|
     puts "**********RESULT #: #{i}**********"
     @cells = life_game
     print_cells()
   end
 end

 def life_game

   result_cells = Array.new(@cells.size) { Array.new(@cells.size) }
   max_cell_size = @cells.size-1
   (0..max_cell_size).each do |v|
     (0..max_cell_size).each do |h|
       result = 0
       if v==0
         result += get_down(v, h)
       end

       if h==0
         result += get_right( v, h)
       end

       if v==0 && h==0
         result += get_left_down(v, h)
       end

       if v>0 && v<max_cell_size
         result += get_up( v, h) + get_down(v, h)
       end

       if h>0 && h<max_cell_size

         result += get_left( v, h) + get_right( v, h)
       end

       if h>0 && h<max_cell_size && v==0
         result += get_left_down(v, h) + get_right_down( v, h)
       end

       if h>0 && h<max_cell_size && v==max_cell_size
         result += get_left_up(v, h) + get_right_up(v, h)
       end

       if v>0 && v<max_cell_size && h==0
         result += get_right_up(v, h) + get_right_down(v, h)
       end

       if v>0 && v<max_cell_size && h==max_cell_size
         result += get_left_up(v, h) + get_left_down(v, h)
       end

       if h>0 && h<max_cell_size && v>0 && v<max_cell_size
         result += get_left_up(v, h) + get_right_up(v, h) + get_left_down(v, h) + get_right_down(v, h)
       end

       if v==max_cell_size
         result += get_up(v, h)
       end

       if h==max_cell_size
         result += get_left(v, h)
       end

       if v==max_cell_size && h==max_cell_size
         result += get_left_up(v, h)
       end

       'puts "resultado v:#{v} h:#{h} r:#{result}"'
       if result == 2 || result == 3
         result_cells[v][h] = 1
       else
         result_cells[v][h] = 0
       end

     end
   end

   return result_cells
 end

 def print_cells()
   max_cell_size = @cells.size-1
   (0..max_cell_size).each do |v|
     (0..max_cell_size).each do |h|
       if h<max_cell_size
         print "#{@cells[v][h]}-"
       else
         print "#{@cells[v][h]}"
       end
     end
     puts "\n"
   end
 end

 def get_right(v, h)
   @cells[v][h+1]
 end

 def get_down(v, h)
   @cells[v+1][h]
 end

 def get_up(v, h)
   @cells[v-1][h]
 end

 def get_left(v, h)
   @cells[v][h-1]
 end

 def get_left_up(v, h)
   @cells[v-1][h-1]
 end

 def get_left_down(v, h)
   @cells[v+1][h-1]
 end

 def get_right_up(v, h)
   @cells[v-1][h+1]
 end

 def get_right_down(v, h)
   @cells[v+1][h+1]
 end
end

arr = [[0,0,1,1],[1,0,0,0],[1,0,0,1],[1,0,0,1]]
a = LifeGame.new(arr)
a.run(5)