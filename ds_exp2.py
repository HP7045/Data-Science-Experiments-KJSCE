import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Weather Dataset",
    filetypes=[
        ("Excel files", "*.xlsx *.xls"),
        ("All files", "*.*")
    ]
)

if not file_path:
    print("No file selected.")
    exit()

df = pd.read_excel(file_path)

print("\n" + "=" * 70)
print("1. READING DATASET")
print("=" * 70)
print(df.head())
print("\nObservation: The weather dataset was successfully loaded from the selected Excel file. The first five records provide an overview of the available weather attributes.")

print("\n" + "=" * 70)
print("2. DATASET INFORMATION")
print("=" * 70)
df.info()
print("\nObservation: The dataset structure, number of records, column names, data types, and non-null counts were obtained.")

print("\n" + "=" * 70)
print("3. DATASET DESCRIPTION")
print("=" * 70)
print(df.describe(include="all"))
print("\nObservation: Statistical measures such as count, mean, standard deviation, minimum, maximum, and quartile values were obtained for the dataset.")

print("\nDataset shape:", df.shape)
print("\nObservation: The dataset dimensions show the total number of observations and attributes available for analysis.")

print("\nColumn names:")
print(df.columns.tolist())
print("\nObservation: All attributes present in the weather dataset were identified.")

print("\n" + "=" * 70)
print("4. NULL VALUE ANALYSIS")
print("=" * 70)
print(df.isnull().sum())
print("\nTotal null values:", df.isnull().sum().sum())
print("\nObservation: The number of missing values in each column and the total number of missing values in the dataset were identified.")

numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df.fillna({col: df[col].median()}, inplace=True)

categorical_columns = df.select_dtypes(include="object").columns

for col in categorical_columns:
    if df[col].isnull().sum() > 0:
        df.fillna({col: df[col].mode()[0]}, inplace=True)

print("\n" + "=" * 70)
print("5. MISSING VALUE IMPUTATION")
print("=" * 70)
print(df.isnull().sum())
print("\nObservation: Missing numerical values were replaced using median values and missing categorical values were replaced using their mode. The dataset was rechecked after imputation.")

top_temperature = df.sort_values(
    by="temperature_c",
    ascending=False
).head(8)

print("\n" + "=" * 70)
print("6. TOP 8 HIGHEST TEMPERATURE RECORDS")
print("=" * 70)
print(
    top_temperature[
        ["city", "temperature_c", "relative_humidity", "weather"]
    ]
)
print("\nObservation: The eight records with the highest recorded temperatures were identified by sorting the temperature column in descending order.")

high_temp_humidity = df[
    (df["temperature_c"] > df["temperature_c"].mean()) &
    (df["relative_humidity"] > df["relative_humidity"].mean())
].sort_values(
    by=["temperature_c", "relative_humidity"],
    ascending=False
).head(8)

print("\n" + "=" * 70)
print("7. TOP 8 HIGH TEMPERATURE AND HUMIDITY RECORDS")
print("=" * 70)
print(
    high_temp_humidity[
        ["city", "temperature_c", "relative_humidity", "weather"]
    ]
)
print("\nObservation: Records having both above-average temperature and above-average humidity were filtered and sorted to identify relatively hot and humid conditions.")

print("\n" + "=" * 70)
print("8. FREQUENCY OF WEATHER CONDITIONS")
print("=" * 70)
print(df["weather"].value_counts())
print("\nObservation: The frequency of each weather condition was calculated, showing how frequently different weather conditions occur in the dataset.")

print("\n" + "=" * 70)
print("9. FREQUENCY OF PRECIPITATION TYPES")
print("=" * 70)
print(df["precipitation_type"].value_counts())
print("\nObservation: The frequency of different precipitation types was calculated to determine their occurrence in the dataset.")

sorted_rows = df.sort_values(
    by="wind_speed",
    ascending=False
)

print("\n" + "=" * 70)
print("10. SORTING ROWS BY WIND SPEED")
print("=" * 70)
print(
    sorted_rows[
        ["city", "wind_speed", "wind_direction", "temperature_c"]
    ].head(10)
)
print("\nObservation: The records were sorted according to wind speed, allowing the observations with the strongest winds to be identified.")

sorted_columns = df.reindex(
    sorted(df.columns),
    axis=1
)

print("\n" + "=" * 70)
print("11. SORTING COLUMNS")
print("=" * 70)
print(sorted_columns.head())
print("\nObservation: The columns were reordered alphabetically to demonstrate column-wise sorting.")

print("\n" + "=" * 70)
print("12. IMPLICIT INDEXING")
print("=" * 70)

print("\nFirst record:")
print(df.iloc[0])

print("\nFirst 5 records:")
print(df.iloc[0:5])

print("\nTemperature and humidity of first 5 records:")
print(
    df.iloc[0:5][
        ["temperature_c", "relative_humidity"]
    ]
)

print("\nObservation: Integer-based implicit indexing using iloc was used to access specific rows and selected columns.")

print("\n" + "=" * 70)
print("13. EXPLICIT INDEXING")
print("=" * 70)

print("\nRecord at index 10:")
print(df.loc[10])

print("\nSelected columns at index 10:")
print(
    df.loc[
        10,
        ["city", "temperature_c", "relative_humidity"]
    ]
)

print("\nObservation: Label-based explicit indexing using loc was used to access a particular record and selected attributes.")

case1 = df[
    df["temperature_c"] > 35
][
    ["city", "temperature_c", "weather"]
]

print("\n" + "=" * 70)
print("14. CONDITIONAL FILTERING - CASE 1")
print("=" * 70)
print(case1.head(10))
print("\nObservation: Records with temperatures greater than 35°C were extracted, identifying relatively hot weather conditions.")

case2 = df[
    (df["temperature_c"] > 30) &
    (df["relative_humidity"] > 70)
][
    ["city", "temperature_c", "relative_humidity"]
]

print("\n" + "=" * 70)
print("15. CONDITIONAL FILTERING - CASE 2")
print("=" * 70)
print(case2.head(10))
print("\nObservation: Records satisfying both high-temperature and high-humidity conditions were identified using a compound condition.")

case3 = df[
    (
        (df["wind_speed"] > 15) &
        (df["precipitation_amount"] > 5)
    ) |
    (df["temperature_c"] > 40)
][
    [
        "city",
        "temperature_c",
        "wind_speed",
        "precipitation_amount"
    ]
]

print("\n" + "=" * 70)
print("16. CONDITIONAL FILTERING - CASE 3")
print("=" * 70)
print(case3.head(10))
print("\nObservation: Records with high wind and precipitation or extremely high temperature were identified using compound logical conditions.")

weather_columns = [
    "temperature_c",
    "relative_humidity",
    "wind_speed",
    "precipitation_amount",
    "cloud_cover",
    "lifted_index"
]

print("\n" + "=" * 70)
print("17. MINIMUM VALUES")
print("=" * 70)
print(df[weather_columns].min())
print("\nObservation: The minimum values of important weather parameters were calculated to identify the lowest recorded conditions.")

print("\n" + "=" * 70)
print("18. MAXIMUM VALUES")
print("=" * 70)
print(df[weather_columns].max())
print("\nObservation: The maximum values of important weather parameters were calculated to identify the highest recorded conditions.")

print("\nMinimum temperature:")
print(df["temperature_c"].min())

print("\nMaximum temperature:")
print(df["temperature_c"].max())

print("\nCity with maximum temperature:")
print(
    df.loc[
        df["temperature_c"].idxmax(),
        "city"
    ]
)

print("\nCity with minimum temperature:")
print(
    df.loc[
        df["temperature_c"].idxmin(),
        "city"
    ]
)

print("\nObservation: The minimum and maximum temperature values were identified along with the cities associated with these extreme observations.")

city_group = df.groupby("city")[
    [
        "temperature_c",
        "relative_humidity",
        "wind_speed"
    ]
].mean()

print("\n" + "=" * 70)
print("19. GROUP BY CITY")
print("=" * 70)
print(city_group)
print("\nObservation: Weather parameters were grouped by city and their average values were calculated, allowing comparison of weather conditions among cities.")

city_weather_group = df.groupby(
    ["city", "weather"]
)[
    [
        "temperature_c",
        "relative_humidity"
    ]
].mean()

print("\n" + "=" * 70)
print("20. GROUP BY CITY AND WEATHER")
print("=" * 70)
print(city_weather_group)
print("\nObservation: Data was grouped simultaneously by city and weather condition to examine temperature and humidity for specific city-weather combinations.")

df["temperature_f"] = (
    df["temperature_c"] * 9 / 5
) + 32

print("\n" + "=" * 70)
print("21. ADDING NEW COLUMN - TEMPERATURE IN FAHRENHEIT")
print("=" * 70)
print(
    df[
        ["temperature_c", "temperature_f"]
    ].head()
)
print("\nObservation: A new temperature_f column was created by converting the existing Celsius temperature values into Fahrenheit.")

df["temperature_wind_index"] = (
    df["temperature_c"] * df["wind_speed"]
)

print("\n" + "=" * 70)
print("22. ADDING NEW DERIVED COLUMN")
print("=" * 70)
print(
    df[
        [
            "temperature_c",
            "wind_speed",
            "temperature_wind_index"
        ]
    ].head()
)
print("\nObservation: A new temperature-wind index was generated using existing temperature and wind-speed values.")

city_aggregate = df.groupby("city").agg(
    average_temperature=("temperature_c", "mean"),
    minimum_temperature=("temperature_c", "min"),
    maximum_temperature=("temperature_c", "max"),
    average_humidity=("relative_humidity", "mean"),
    average_wind_speed=("wind_speed", "mean")
)

print("\n" + "=" * 70)
print("23. AGGREGATE FUNCTIONS WITH GROUPBY - CASE 1")
print("=" * 70)
print(city_aggregate)
print("\nObservation: Multiple aggregate functions were applied to city groups to obtain average, minimum, maximum, and other weather statistics.")

weather_aggregate = df.groupby("weather").agg(
    average_temperature=("temperature_c", "mean"),
    maximum_temperature=("temperature_c", "max"),
    average_humidity=("relative_humidity", "mean"),
    total_precipitation=("precipitation_amount", "sum"),
    record_count=("weather", "count")
)

print("\n" + "=" * 70)
print("24. AGGREGATE FUNCTIONS WITH GROUPBY - CASE 2")
print("=" * 70)
print(weather_aggregate)
print("\nObservation: Weather conditions were summarized using mean, maximum, sum, and count aggregate functions.")

selected_city = "Mumbai"

if selected_city in df["city"].values:

    selected_group = df.groupby("city").get_group(
        selected_city
    )

    print("\n" + "=" * 70)
    print("25. SELECTION OF PARTICULAR GROUP")
    print("=" * 70)
    print(
        selected_group[
            [
                "city",
                "temperature_c",
                "relative_humidity",
                "weather"
            ]
        ].head(10)
    )

    print("\nObservation: The records belonging to the selected city, Mumbai, were extracted from the grouped dataset.")

else:

    selected_city = df["city"].iloc[0]

    selected_group = df.groupby("city").get_group(
        selected_city
    )

    print("\n" + "=" * 70)
    print("25. SELECTION OF PARTICULAR GROUP")
    print("=" * 70)
    print(selected_group.head(10))

    print(
        "\nObservation: Mumbai was not available, so the first available city,",
        selected_city,
        "was selected from the grouped dataset."
    )

city_mean_temperature = df.groupby(
    "city"
)["temperature_c"].mean()

hot_cities = city_mean_temperature[
    city_mean_temperature >
    city_mean_temperature.mean()
]

print("\n" + "=" * 70)
print("26. GROUP SELECTION BASED ON CONDITION")
print("=" * 70)
print(hot_cities)
print("\nObservation: Cities having an average temperature greater than the overall average city temperature were identified.")

correlation = df[
    [
        "temperature_c",
        "relative_humidity"
    ]
].corr()

print("\n" + "=" * 70)
print("27. CORRELATION BETWEEN TEMPERATURE AND HUMIDITY")
print("=" * 70)
print(correlation)

temperature_humidity_corr = df["temperature_c"].corr(
    df["relative_humidity"]
)

print(
    "\nCorrelation coefficient:",
    temperature_humidity_corr
)

print("\nObservation: The correlation coefficient indicates the strength and direction of the relationship between temperature and relative humidity.")

temperature_wind_corr = df["temperature_c"].corr(
    df["wind_speed"]
)

print("\n" + "=" * 70)
print("28. CORRELATION BETWEEN TEMPERATURE AND WIND SPEED")
print("=" * 70)
print("Correlation coefficient:", temperature_wind_corr)
print("\nObservation: The correlation coefficient was calculated to determine the relationship between temperature and wind speed.")

df["temperature_normalized"] = (
    df["temperature_c"] -
    df["temperature_c"].min()
) / (
    df["temperature_c"].max() -
    df["temperature_c"].min()
)

df["humidity_normalized"] = (
    df["relative_humidity"] -
    df["relative_humidity"].min()
) / (
    df["relative_humidity"].max() -
    df["relative_humidity"].min()
)

print("\n" + "=" * 70)
print("29. MIN-MAX NORMALIZATION")
print("=" * 70)
print(
    df[
        [
            "temperature_c",
            "temperature_normalized",
            "relative_humidity",
            "humidity_normalized"
        ]
    ].head(10)
)
print("\nObservation: Temperature and humidity were normalized using Min-Max normalization, scaling their values to a range between 0 and 1.")

city_info = df[
    [
        "city",
        "latitude",
        "longitude"
    ]
].drop_duplicates(
    subset="city"
)

city_info["region"] = "India"

df_joined = df.merge(
    city_info,
    on=["city", "latitude", "longitude"],
    how="left"
)

print("\n" + "=" * 70)
print("30. JOINING DATAFRAMES")
print("=" * 70)
print(
    df_joined[
        [
            "city",
            "latitude",
            "longitude",
            "region"
        ]
    ].head(10)
)
print("\nObservation: Additional city information was joined with the weather dataset using common city and geographical attributes.")

city_summary = df.groupby("city").agg(
    average_temperature=("temperature_c", "mean"),
    average_humidity=("relative_humidity", "mean")
).reset_index()

city_details = df[
    [
        "city",
        "latitude",
        "longitude"
    ]
].drop_duplicates(
    subset="city"
)

merged_data = pd.merge(
    city_summary,
    city_details,
    on="city",
    how="inner"
)

print("\n" + "=" * 70)
print("31. MERGING DATAFRAMES")
print("=" * 70)
print(merged_data.head(10))
print("\nObservation: City-level weather summaries were merged with geographical details to create a combined DataFrame.")

part1 = df.head(5)
part2 = df.tail(5)

concatenated_rows = pd.concat(
    [part1, part2],
    axis=0
)

print("\n" + "=" * 70)
print("32. ROW-WISE CONCATENATION")
print("=" * 70)
print(concatenated_rows)
print("\nObservation: Two portions of the DataFrame were concatenated vertically to demonstrate row-wise combination of data.")

extra_data = pd.DataFrame({
    "data_source": ["India Weather Dataset"] * len(df)
})

concatenated_columns = pd.concat(
    [
        df.reset_index(drop=True),
        extra_data
    ],
    axis=1
)

print("\n" + "=" * 70)
print("33. COLUMN-WISE CONCATENATION")
print("=" * 70)
print(concatenated_columns.head())
print("\nObservation: An additional data-source column was concatenated horizontally with the existing dataset.")

print("\n" + "=" * 70)
print("34. FINAL PROCESSED DATASET")
print("=" * 70)

print(df.head())

print("\nFinal shape:")
print(df.shape)

print("\nFinal columns:")
print(df.columns.tolist())

print("\nFinal null value check:")
print(df.isnull().sum())

print("\nObservation: The final dataset contains the original weather attributes along with newly generated columns. The final null-value check confirms that missing values have been handled.")

save_path = filedialog.asksaveasfilename(
    title="Save Analysed Dataset",
    defaultextension=".xlsx",
    filetypes=[
        ("Excel files", "*.xlsx"),
        ("All files", "*.*")
    ]
)

if save_path:
    df.to_excel(
        save_path,
        index=False
    )

    print("\n" + "=" * 70)
    print("35. EXPORTING PROCESSED DATASET")
    print("=" * 70)
    print("File saved at:", save_path)
    print("\nObservation: The fully processed and analyzed dataset was successfully exported to an Excel file for future use.")
else:
    print("\nObservation: The output file was not saved because no save location was selected.")

root.destroy()

print("\n" + "=" * 70)
print("OVERALL OBSERVATION")
print("=" * 70)
print("The experiment successfully demonstrated data loading, exploration,")
print("cleaning, filtering, sorting, indexing, frequency analysis, grouping,")
print("aggregation, feature creation, correlation, normalization, joining,")
print("merging, concatenation, and exporting using NumPy and Pandas.")
print("The weather dataset was transformed into a structured form suitable")
print("for further data analysis and AI-based weather prediction applications.")