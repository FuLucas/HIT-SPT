import org.junit.Test;

import static org.junit.Assert.*;

public class StudentTest {

    @Test
    public void getName() {
        Student stu = new Student("fhd", 11902);
        assertEquals(stu.getName(), "fhd");
    }

    @Test
    public void getId() {
        Student stu = new Student("fhd", 11902);
        assertEquals(stu.getId(), 11902);
    }

    @Test
    public void addScore() {
        Student stu = new Student("fhd", 11902);
        assertFalse(stu.addScore("", 98));
        assertTrue(stu.addScore("Math", 98));
        assertFalse(stu.addScore("Math", 70));
        assertFalse(stu.addScore("English", -1));
        assertTrue(stu.addScore("English", 0));
        assertTrue(stu.addScore("Chines", 1));
        assertTrue(stu.addScore("PE", 99));
        assertTrue(stu.addScore("chemistry", 100));
        assertFalse(stu.addScore("python", 101));
    }

    @Test
    public void getAverageScore() {
        Student stu = new Student("fhd", 11902);
        assertEquals(stu.getAverageScore(), 0, 0.01);
        assertTrue(stu.addScore("Math", 98));
        assertEquals(stu.getAverageScore(), 98, 0.01);
        assertTrue(stu.addScore("Chines", 80));
        assertEquals(stu.getAverageScore(), 89, 0.01);
        assertTrue(stu.addScore("python", 95));
        assertEquals(stu.getAverageScore(), 91, 0.01);
        assertTrue(stu.addScore("PE", 82));
        assertEquals(stu.getAverageScore(), 88.75, 0.01);
    }

    @Test
    public void getScore() {
        Student stu = new Student("fhd", 11902);
        assertTrue(stu.addScore("Math", 98));
        assertTrue(stu.addScore("Chines", 80));
        assertTrue(stu.addScore("python", 95));
        assertTrue(stu.addScore("PE", 82));
        assertEquals(stu.getScore("Math"), 98);
        assertEquals(stu.getScore("Chines"), 80);
        assertEquals(stu.getScore("test"), -1);
        assertEquals(stu.getScore(""), -1);
        assertEquals(stu.getScore(null), -1);
    }

    @Test
    public void getScores() {
        Student stu = new Student("fhd", 11902);
        assertEquals(stu.getScores().size(), 0);
        assertTrue(stu.addScore("Math", 98));
        assertTrue(stu.addScore("Chines", 80));
        assertTrue(stu.addScore("python", 95));
        assertTrue(stu.addScore("PE", 82));
        assertEquals(stu.getScores().size(), 4);
    }

    @Test
    public void toStringTest() {
        Student stu1 = new Student("fhd", 11901);
        Student stu2 = new Student("", 11902);
        Student stu3 = new Student(" ", 11903);
        assertEquals(stu1.toString(), "name=fhd, id=11901");
        assertEquals(stu2.toString(), "name=, id=11902");
        assertEquals(stu3.toString(), "name= , id=11903");
    }

}