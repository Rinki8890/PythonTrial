import java.io.*; 
import java.util.*; 
import java.lang.*;

class Pair {
    int x,y;
    Pair(){
        this.x=0;
        this.y=0;
    }
    Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class GFG {
    
    static void sortPair(Pair arr[], int n) {
        Arrays.sort(arr, new Comparator<Pair>() { 
            @Override public int compare(Pair p1, Pair p2) { 
                return p1.x - p2.x; 
            } 
        }); 
    }
	
	public static void main (String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
		    String inputLine[] = br.readLine().trim().split(" ");
		    int n = Integer.parseInt(inputLine[0]);
		    Pair[] p = new Pair[n];
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        p[i] = new Pair();
		        p[i].y = Integer.parseInt(inputLine[i]);    // Putting the starting time as y.
		    }
		    inputLine = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++){
		        p[i].x = Integer.parseInt(inputLine[i]);       // Putting the finshing time as x.
		    }
		    sortPair(p, n);             // Now if we sort, it will sort according to the finish time.
		    int i=0, j=1, ans=1;
		    while(i<n && j<n){
		        if(p[i].x<=p[j].y){    // If the last ended time is less than the next item starting time.
		            i=j;
		            j++;
		            ans++;
		        } else {
		            j++;
		        }
		    }
		    System.out.println(ans);
		}
	}
}