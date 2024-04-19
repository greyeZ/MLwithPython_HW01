import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF

# Formula 1 Tracks Data from  https://en.wikipedia.org/wiki/List_of_Formula_One_circuits as Formula 1
f1_tracks_data = {
    'Circuit': ['Adelaide Street Circuit', 'Ain-Diab Circuit', 'Aintree Motor Racing Circuit',
                'Albert Park Circuit *', 'Algarve International Circuit', 'Autódromo do Estoril',
                'Autódromo Hermanos Rodríguez *', 'Autódromo Internacional do Rio de Janeiro',
                'Autodromo Internazionale del Mugello', 'Autodromo Internazionale Enzo e Dino Ferrari *',
                'Autódromo José Carlos Pace *', 'Autodromo Nazionale di Monza *', 'Autódromo Oscar y Juan Gálvez',
                'AVUS', 'Bahrain International Circuit *', 'Baku City Circuit *', 'Brands Hatch Circuit',
                'Buddh International Circuit', 'Bugatti Au Mans', 'Caesars Palace Grand Prix Circuit',
                'Charade Circuit', 'Circuit Bremgarten', 'Circuit de Barcelona-Catalunya *', 'Circuit de Monaco *',
                'Circuit de Nevers Magny-Cours', 'Circuit de Pedralbes', 'Circuit de Reims-Gueux',
                'Circuit de Spa-Francorchamps *', 'Circuit Dijon-Prenois', 'Circuit Gilles-Villeneuve *',
                'Circuit Mont-Tremblant', 'Circuit of the Americas *', 'Circuit Paul Ricard', 'Circuit Zandvoort *',
                'Circuit Zolder', 'Circuito da Boavista', 'Circuito de Monsanto', 'Circuito Permanente de Jerez',
                'Circuito Permanente del Jarama', 'Dallas Fair Park', 'Detroit Street Circuit', 'Donington Park',
                'Fuji Speedway', 'Hockenheimring', 'Hungaroring *', 'Indianapolis Motor Speedway',
                'Intercity Istanbul Park', 'Jeddah Corniche Circuit *', 'Korea International Circuit',
                'Kyalami Grand Prix Circuit', 'Las Vegas Strip Circuit *', 'Long Beach Street Circuit',
                'Lusail International Circuit *', 'Marina Bay Street Circuit *', 'Miami International Autodrome *',
                'Montjuïc circuit', 'Mosport International Raceway', 'Nivelles-Baulers', 'Nürburgring',
                'Pescara Circuit', 'Phoenix Street Circuit', 'Prince George Circuit', 'Red Bull Ring *',
                'Riverside International Raceway', 'Rouen-Les-Essarts', 'Scandinavian Raceway', 'Sebring Raceway',
                'Sepang International Circuit', 'Shanghai International Circuit *', 'Silverstone Circuit *',
                'Sochi Autodrom', 'Suzuka International Racing Course *', 'TI Circuit Aida',
                'Valencia Street Circuit', 'Watkins Glen International', 'Yas Marina Circuit *',
                'Zeltweg Airfield'],
    'Country': ['Australia', 'Morocco', 'United Kingdom', 'Australia', 'Portugal', 'Portugal', 'Mexico', 'Brazil',
                'Italy',
                'Italy', 'Brazil', 'Italy', 'Argentina', 'Germany', 'Bahrain', 'Azerbaijan', 'United Kingdom', 'India',
                'France', 'United States', 'France', 'Switzerland', 'Spain', 'Monaco', 'France', 'Spain', 'France',
                'Belgium', 'France', 'Canada', 'Canada', 'United States', 'France', 'Netherlands', 'Belgium',
                'Portugal', 'Portugal', 'Spain', 'Spain', 'United States', 'United States', 'United Kingdom',
                'Japan', 'Germany', 'Hungary', 'United States', 'Turkey', 'Saudi Arabia', 'South Korea', 'South Africa',
                'United States', 'United States', 'Qatar', 'Singapore', 'United States', 'Spain', 'Canada',
                'Belgium', 'Germany', 'Italy', 'United States', 'United States', 'Canada', 'Austria', 'United States',
                'France', 'Sweden', 'United States', 'Malaysia', 'China', 'United Kingdom', 'Russia', 'Japan', 'Japan',
                'Spain', 'United Kingdom', 'United Arab Emirates', 'Austria']
}

# NASCAR Tracks Data from  https://www.nascar.com/tracks/
nascar_tracks_data = {
    'Track': ['Atlanta Motor Speedway', 'Auto Club Speedway', 'Bristol Motor Speedway', 'Charlotte Motor Speedway',
              'Chicagoland Speedway', 'Daytona International Speedway *', 'Darlington Raceway',
              'Dover International Speedway', 'Homestead-Miami Speedway', 'Indianapolis Motor Speedway *',
              'ISM Raceway',
              'Kansas Speedway', 'Kentucky Speedway', 'Las Vegas Motor Speedway', 'Martinsville Speedway',
              'Michigan International Speedway', 'Nashville Superspeedway *', 'New Hampshire Motor Speedway',
              'North Wilkesboro Speedway', 'Phoenix Raceway', 'Pocono Raceway *', 'Richmond Raceway', 'Road America',
              'Sonoma Raceway *', 'South Boston Speedway', 'Talladega Superspeedway', 'Texas Motor Speedway',
              'Watkins Glen International *', 'World Wide Technology Raceway'],
    'Location': ['Hampton, Georgia', 'Fontana, California', 'Bristol, Tennessee', 'Concord, North Carolina',
                 'Joliet, Illinois', 'Daytona Beach, Florida', 'Darlington, South Carolina', 'Dover, Delaware',
                 'Homestead, Florida', 'Speedway, Indiana', 'Avondale, Arizona', 'Kansas City, Kansas',
                 'Sparta, Kentucky', 'Las Vegas, Nevada', 'Martinsville, Virginia', 'Brooklyn, Michigan',
                 'Lebanon, Tennessee', 'Loudon, New Hampshire', 'North Wilkesboro, North Carolina',
                 'Avondale, Arizona', 'Long Pond, Pennsylvania', 'Richmond, Virginia', 'Elkhart Lake, Wisconsin',
                 'Sonoma, California', 'South Boston, Virginia', 'Lincoln, Alabama', 'Fort Worth, Texas',
                 'Watkins Glen, New York', 'Madison, Illinois'],
    'Length': ['1.54 mi (2.48 km)', '2.0 mi (3.22 km)', '0.533 mi (0.858 km)', '1.5 mi (2.41 km)',
               '1.5 mi (2.41 km)', '2.5 mi (4.02 km)', '1.366 mi (2.198 km)', '1 mi (1.61 km)', '1.5 mi (2.41 km)',
               '2.5 mi (4.02 km)', '1 mi (1.61 km)', '1.5 mi (2.41 km)', '1.5 mi (2.41 km)', '1.5 mi (2.41 km)',
               '0.526 mi (0.847 km)', '2 mi (3.22 km)', '1.33 mi (2.14 km)', '1.058 mi (1.703 km)',
               '0.625 mi (1.006 km)', '1 mi (1.61 km)', '2.5 mi (4.02 km)', '0.75 mi (1.21 km)',
               '4.048 mi (6.515 km)', '2.52 mi (4.06 km)', '0.4 mi (0.64 km)', '2.66 mi (4.28 km)',
               '2.45 mi (3.95 km)', '2.45 mi (3.95 km)', '1.25 mi (2.01 km)'],
    'Surface': ['Asphalt', 'Asphalt', 'Concrete', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Concrete',
                'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Concrete',
                'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt', 'Asphalt',
                'Asphalt', 'Concrete', 'Asphalt'],
    'Turns': ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4', '4',
              '3', '4', '14', '12', '4', '4', '4', '12', '4']
}

# Formula E Tracks Data from ChatGPT
formula_e_tracks_data = {
    'Circuit': ['Ad Diriyah Street Circuit', 'Albert Park Street Circuit', 'Autódromo Hermanos Rodríguez',
                'Battersea Park Street Circuit', 'Beijing Olympic Green Circuit',
                'Berlin Tempelhof Airport Street Circuit', 'Circuit Ricardo Tormo', 'Circuit des Invalides',
                'Circuit Moulay El Hassan', 'Circuit Park Zandvoort', 'Circuito Cittadino dell\'EUR',
                'Circuito de Punta del Este', 'Circuito de Velocidad Callejero', 'Circuit de Monaco',
                'Circuit Trois-Rivières', 'City Walk Street Circuit', 'ExCeL London Street Circuit',
                'Hermanos Rodríguez Street Circuit', 'Hong Kong Central Harbourfront Circuit',
                'Huangpu Park Street Circuit', 'Long Beach Street Circuit', 'Marina Bay Street Circuit',
                'Marina Circuit', 'Mexico City Street Circuit', 'Monte Carlo Street Circuit', 'Moscow Street Circuit',
                'Paris Street Circuit', 'Putrajaya Street Circuit', 'Red Hook Street Circuit', 'Riyadh Street Circuit',
                'Rome Street Circuit', 'Seoul Street Circuit', 'Suzuka Street Circuit',
                'Templehof Airport Street Circuit',
                'Valencia Street Circuit', 'Yas Marina Circuit'],
    'Country': ['Saudi Arabia', 'Australia', 'Mexico', 'United Kingdom', 'China', 'Germany', 'Spain', 'France',
                'Morocco', 'Netherlands', 'Italy', 'Uruguay', 'Argentina', 'Monaco', 'Canada', 'United Arab Emirates',
                'United Kingdom', 'Mexico', 'Hong Kong', 'China', 'United States', 'Singapore', 'Qatar', 'Mexico',
                'Monaco', 'Russia', 'France', 'Malaysia', 'United States', 'Saudi Arabia', 'Italy', 'South Korea',
                'Japan',
                'Germany', 'Spain', 'United Arab Emirates']
}

# IndyCar Series Drivers Data https://en.wikipedia.org/wiki/List_of_IndyCar_Series_drivers
indycar_drivers_data = {
    'Driver': ['Kyle Larson', 'Chase Elliott', 'Martin Truex Jr.', 'Kevin Harvick', 'Denny Hamlin', 'Joey Logano',
               'Ryan Blaney', 'William Byron', 'Kyle Busch', 'Alex Bowman', 'Austin Dillon', 'Christopher Bell',
               'Brad Keselowski', 'Tyler Reddick', 'Kurt Busch', 'Michael McDowell', 'Ryan Newman', 'Erik Jones',
               'Ricky Stenhouse Jr.', 'Chris Buescher', 'Matt DiBenedetto'],
    'Nationality': ['American', 'American', 'American', 'American', 'American', 'American', 'American', 'American',
                    'American', 'American', 'American', 'American', 'American', 'American', 'American', 'American',
                    'American', 'American', 'American', 'American', 'American'],
    'Team': ['Hendrick Motorsports', 'Hendrick Motorsports', 'Joe Gibbs Racing', 'Stewart-Haas Racing',
             'Joe Gibbs Racing', 'Team Penske', 'Team Penske', 'Hendrick Motorsports', 'Joe Gibbs Racing',
             'Hendrick Motorsports', 'Richard Childress Racing', 'Joe Gibbs Racing', 'RFK Racing',
             'Richard Childress Racing', '23XI Racing', 'Front Row Motorsports', 'RFK Racing', 'Petty GMS Motorsports',
             'JTG Daugherty Racing', 'Roush Fenway Racing', 'Wood Brothers Racing']
}

# Formula 1 Drivers Data from https://www.statsf1.com/en/pilotes.aspx
formula_1_drivers_data = {
    'Driver': ['Lewis Hamilton', 'Sebastian Vettel', 'Fernando Alonso', 'Max Verstappen', 'Sergio Perez',
               'Charles Leclerc', 'Daniel Ricciardo', 'Valtteri Bottas', 'Kimi Räikkönen', 'Nico Hülkenberg',
               'Carlos Sainz Jr.', 'Lando Norris', 'Esteban Ocon', 'Pierre Gasly', 'Lance Stroll', 'George Russell',
               'Yuki Tsunoda', 'Antonio Giovinazzi', 'Nicholas Latifi', 'Mick Schumacher', 'Nikita Mazepin'],
    'Nationality': ['British', 'German', 'Spanish', 'Dutch', 'Mexican', 'Monegasque', 'Australian', 'Finnish',
                    'Finnish', 'German', 'Spanish', 'British', 'French', 'French', 'Canadian', 'British', 'Japanese',
                    'Italian', 'Canadian', 'German', 'Russian'],
    'Team': ['Mercedes', 'Aston Martin', 'Alpine', 'Red Bull Racing', 'Red Bull Racing', 'Ferrari', 'McLaren',
             'Alfa Romeo Racing', 'Alfa Romeo Racing', 'Aston Martin', 'Ferrari', 'McLaren', 'Alpine', 'AlphaTauri',
             'Aston Martin', 'Williams', 'AlphaTauri', 'Alfa Romeo Racing', 'Williams', 'Haas', 'Haas']
}


def save_data(df, filename_prefix):
    df.to_xml(f"{filename_prefix}.xml", index=False)
    df.to_json(f"{filename_prefix}.json", orient="records")

def fill_and_scale_data(df):
    from sklearn.preprocessing import StandardScaler
    df = df.fillna(df.mean(numeric_only=True))
    numeric_cols = df.select_dtypes(include=[np.number])
    if not numeric_cols.empty:
        scaler = StandardScaler()
        df[numeric_cols.columns] = scaler.fit_transform(numeric_cols)
    return df

def create_pivot_table(df, index, values, aggfunc):
    pivot_table = df.pivot_table(index=index, values=values, aggfunc=aggfunc)
    save_data(pivot_table, f"pivot_{index}_vs_{values}")
    return pivot_table

def statistical_analysis(df):
    stats_summary = df.describe()
    correlation_matrix = df.corr()

    with open("stats_summary.txt", "w") as file:
        file.write(f"Statistical Summary:\n{stats_summary}\n\nCorrelation Matrix:\n{correlation_matrix}\n")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Statistical Summary and Correlation Matrix", ln=True, align="C")
    pdf.cell(200, 10, txt=str(stats_summary), ln=True, align="L")
    pdf.cell(200, 10, txt=str(correlation_matrix), ln=True, align="L")
    pdf.output("stats_summary.pdf")

def plot_visualization(df, x_column, y_column, plot_type, filename):
    plt.figure(figsize=(10, 6))
    if plot_type == 'bar':
        sns.barplot(x=x_column, y=y_column, data=df)
    elif plot_type == 'histogram':
        sns.histplot(df[x_column], kde=True)
    elif plot_type == 'scatter':
        sns.scatterplot(x=x_column, y=y_column, data=df)

    plt.title(f'{plot_type.title()} of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{filename}.jpg")
    plt.close()

    # Save plot to PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.image(f"{filename}.jpg", x=10, y=8, w=180)
    pdf.output(f"{filename}.pdf")

def data_processing(tracks_df, drivers_df):
    tracks_df = fill_and_scale_data(tracks_df)
    save_data(tracks_df, "processed_tracks")

    pivot_table = create_pivot_table(tracks_df, 'Country', 'Circuit', aggfunc='count')

    statistical_analysis(tracks_df)

    plot_visualization(tracks_df, 'Country', 'Circuit', 'scatter', 'tracks_by_country')
    plot_visualization(tracks_df, 'Circuit', None, 'histogram', 'circuit_length_distribution')
    plot_visualization(drivers_df, 'Nationality', None, 'bar', 'drivers_nationality')

    return tracks_df, drivers_df, pivot_table

# Main function call
if __name__ == '__main__':
    try:
        tracks_df, drivers_df, pivot_table = data_processing(tracks_df, drivers_df)
    except Exception as e:
        print(f"Error during data processing: {e}")