package DataStructures;

import java.sql.SQLOutput;
import java.util.*;

public class bestAlbum {
    public static void main(String[] args) {
        int[] plays = {500, 600, 150, 800, 2500};
        String[] genres ={"classic", "pop", "classic", "classic", "pop"};
        System.out.println(Arrays.toString(solution(genres, plays)));
    }

    public static int[] solution(String[] genres, int[] plays) {
        Map<String, List<Integer>> map = new HashMap<>();
        Map<String, Genre> genreList = new HashMap<>();


        for (int i = 0; i < genres.length; i++) {

            if (map.containsKey(genres[i])) {
                for (String key: genreList.keySet()) {
                    System.out.println("key: " + key);
                    System.out.println("value" + genreList.get(key).getName());
                }

                System.out.println("Genre: " + genres[i]);
                System.out.println(genreList.get(genres[i]).getName());
                if (genres[i].equals("classic")) {
                    genreList.get("classic").addSong();
                }
                System.out.println("added Genre: " + genreList.get(genres[i]).getName());

                List<Integer> songs = map.get(genres[i]);
                if (songs.size() == 1) {
                    songs.add(i);
                    if (plays[songs.get(0)] < plays[songs.get(1)]) {
                        int temp = songs.get(1);
                        songs.set(1, songs.get(0));
                        songs.set(0, temp);
                    }
                } else {
                    if (plays[i] > plays[songs.get(1)]) {
                        songs.set(1, i);
                    }
                }
                map.put(genres[i], songs);

            } else {
                Genre g = new Genre(genres[i], 1);
                System.out.println(g.getName());
                genreList.put(genres[i], g);
                //System.out.println(genreList.get(genres[i]).getName());
                System.out.println("Created new Genre named: " + genreList.get(genres[i]).getName());
                List<Integer> ls = new ArrayList<>();
                ls.add(i);
                map.put(genres[i], ls);
                for (String key: genreList.keySet()) {
                    System.out.println("key: " + key);
                    System.out.println("value" + genreList.get(key).getName());
                }

            }
        }
        System.out.println(genreList.keySet());
        for (Genre g: genreList.values()) {
            System.out.print(g.getName() + ", ");
        }
        System.out.println();


        PriorityQueue<Genre> pq = new PriorityQueue<>(new Comparator<Genre>() {
            @Override
            public int compare(Genre g, Genre anotherGenre) {
                if (g.numSongs > anotherGenre.numSongs) {
                    return 1;
                } else if (g.numSongs < anotherGenre.numSongs) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });

        for (String key: genreList.keySet()) {
            System.out.println("key: "+ key);
            pq.add(genreList.get(key));
            System.out.println("Added to PQ Genre.name: " + genreList.get(key).getName());
        }

        List<Integer> answer = new ArrayList<>();

        while (!pq.isEmpty()) {
            Genre g = pq.remove();
            System.out.println(g.getName());
            List<Integer> list = map.get(g.getName());
            for (int i = 0; i < list.size(); i++) {
                answer.add(list.get(i));
            }
        }
        int[] arr = new int[answer.size()];
        return answer.stream().mapToInt(i->i).toArray();

    }

    public static class Genre {
        private static String name;
        private static int numSongs;

        public Genre (String name, int numSongs){
            this.name = name;
            this.numSongs = numSongs;
        }

        public String getName(){
            return this.name;
        }
        public int getNumSongs() {
            return this.getNumSongs();
        }

        public void setNumSongs(int num){
            numSongs = num;
        }

        public void addSong() {
            this.numSongs++;
        }
    }

}
