import java.util.HashSet;
import java.util.Set;
import java.util.HashMap;


public class Student {
    private String name;
    private int id;
    private HashMap<String, Integer> scores = new HashMap<String, Integer>();

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public boolean addScore(String course, int score) {
        if (score > 100 || score < 0 || course.equals("")) {
            return false;
        }
        for (String item : scores.keySet()) {
            if (item.equals(course)) {
                return false;
            }
        }
        scores.put(course, score);
        return true;
    }

    public double getAverageScore() {
        int num = scores.size();
        if (num == 0) {
            return 0;
        }
        else {
            int sumScore = 0;
            for (String item : scores.keySet()) {
                sumScore += scores.get(item);
            }
            return ((double) sumScore) / num;
        }
    }

    public int getScore(String course) {
        for (String item : scores.keySet()) {
            if (item.equals(course)) {
                return scores.get(item);
            }
        }
        return -1;
    }

    public HashMap<String, Integer> getScores() {
        return scores;
    }

    @Override
    public String toString() {
        String result;
        result = "name=" + this.getName() +", id=" + this.getId();
        return result;
    }
}