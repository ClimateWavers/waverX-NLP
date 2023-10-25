import pandas as pd
"""
Clean the dataset by filtering out rows
with target = 0, to filter data to targe = 1 which are disaster related tweets
"""

def filter_data(input_file, output_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Drop rows where target column is 0
    cleaned_df = df[df['target'] != 0]
    # Write cleaned DataFrame back to a CSV file
    cleaned_df.to_csv(output_file, index=False)

    print(f"Cleaned data saved to {output_file}")


def add_data_type(input_file):
    df = pd.read_csv(input_file)
    #Make sure all data are of same type of string
    df['text'] = df['text'].astype(str)
    df['label'] = df['label'].astype(str)
    print("Ensured all data are of type str")
# Example usage
if __name__ == "__main__":
    # Provide input and output file paths
    base_dir = 'dataset'
    disaster_dataset = f"{base_dir}/tweets.csv"
    # Filter Data
    filter_data(disaster_dataset, disaster_dataset)
    add_data_type("dataset/disaster_text.csv")
