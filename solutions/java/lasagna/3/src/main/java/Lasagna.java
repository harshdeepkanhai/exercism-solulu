public class Lasagna {
    
    private static final int LASAGNA_COOK_MINUTES = 40;
    private static final int LASAGNA_LAYER_PREP_MINUTES = 2;
    
    public int expectedMinutesInOven() {
        return LASAGNA_COOK_MINUTES;
    }
    
    public int remainingMinutesInOven(int minutes) {
        return expectedMinutesInOven() - minutes;
    }
    
    public int preparationTimeInMinutes(int layers) {
        return LASAGNA_LAYER_PREP_MINUTES * layers;
    }
    
    public int totalTimeInMinutes(int layers, int minutes) {
        return preparationTimeInMinutes(layers) + minutes;
    }
}
