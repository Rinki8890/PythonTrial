static char maxRepeating(String str) 
    { 
        int len = str.length(); 
        int count = 0; 
  
        // Find the maximum repeating character 
        // starting from str[i] 
        char res = str.charAt(0); 
        if (str.charAt(i) != str.charAt(i+1)) 
            break; 
        else if(str.charAt(i) != str.charAt(i+2))
            break;
        else
            System.out.println("String is NOT Diverse String");
            
        return res; 
    } 

    public static void main(String args[]) 
    { 
  
        String str = "aaa"; 
        System.out.println(maxRepeating(str)); 
    } 

    }