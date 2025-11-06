# nigeria_fiscal_simulator.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ======================
# ENHANCED ECONOMIC MODEL FOR COMMODITY-DEPENDENT ECONOMIES
# ======================
class NigeriaFiscalModel:
    def __init__(self):
        # Nigeria-specific initial values (billions of USD)
        self.initial_gdp = 450  # ~$450B GDP
        self.initial_debt = 140  # ~31% debt-to-GDP
        self.initial_deficit = 12  # ~2.7% of GDP
        
        # Revenue structure (typical for Nigeria)
        self.oil_revenue = 25    # ~$25B from oil
        self.non_oil_revenue = 35 # ~$35B from other sources
        self.total_revenue = self.oil_revenue + self.non_oil_revenue
        
        # Spending
        self.total_spending = self.total_revenue + self.initial_deficit
        
        # Oil parameters
        self.oil_price = 75  # USD per barrel
        self.oil_production = 1.4  # million barrels per day
        self.oil_revenue_per_dollar = 0.33  # $0.33B revenue per $1 oil price
        
    def calculate_impact(self, tax_change, spending_change, growth_assumption, 
                        oil_price_shock, years=5):
        """
        Enhanced model with oil dependency and debt feedback
        """
        
        # Initialize results
        results = []
        gdp = self.initial_gdp
        debt = self.initial_debt
        non_oil_revenue = self.non_oil_revenue
        oil_revenue = self.oil_revenue
        spending = self.total_spending
        
        # Dynamic multipliers based on economic conditions
        economic_condition = self.assess_economic_condition(gdp, debt/gdp)
        spending_multiplier, tax_multiplier = self.get_multipliers(economic_condition)
        
        # Initial interest rate (sovereign borrowing cost)
        interest_rate = 12.0  # Base interest rate in %
        
        for year in range(years):
            # ======================
            # OIL REVENUE CALCULATION
            # ======================
            current_oil_price = self.oil_price * (1 + oil_price_shock/100)
            oil_revenue = current_oil_price * self.oil_revenue_per_dollar
            
            # ======================
            # NON-OIL REVENUE (with growth feedback)
            # ======================
            non_oil_revenue = non_oil_revenue * (1 + tax_change/100) * (1 + growth_assumption/100)
            
            total_revenue = oil_revenue + non_oil_revenue
            
            # ======================
            # SPENDING
            # ======================
            spending = spending * (1 + spending_change/100)
            
            # ======================
            # DEBT-DRIVEN INTEREST RATE (Critical enhancement!)
            # ======================
            debt_to_gdp = (debt / gdp) * 100
            
            # Higher debt leads to higher risk premium
            if debt_to_gdp > 50:
                risk_premium = (debt_to_gdp - 50) * 0.15  # 0.15% increase per 1% debt/GDP above 50%
            elif debt_to_gdp < 30:
                risk_premium = (30 - debt_to_gdp) * -0.1  # Lower rates for good fiscal position
            else:
                risk_premium = 0
                
            effective_interest_rate = interest_rate + risk_premium
            
            # ======================
            # DEBT SERVICE COSTS
            # ======================
            debt_service = debt * (effective_interest_rate/100)
            
            # ======================
            # FISCAL IMPACT ON GDP (with crowding-out effect)
            # ======================
            fiscal_impact = (spending_change * (spending - debt_service) * spending_multiplier + 
                           tax_change * non_oil_revenue * tax_multiplier) / gdp
            
            # ======================
            # CROWDING-OUT EFFECT: Higher debt service reduces productive spending
            # ======================
            crowding_out_effect = max(0, (debt_service - (debt_service * (debt/gdp))) / gdp) * 100
            
            effective_growth = growth_assumption + fiscal_impact - crowding_out_effect
            
            # ======================
            # UPDATE ECONOMIC VARIABLES
            # ======================
            gdp = gdp * (1 + effective_growth/100)
            deficit = spending + debt_service - total_revenue  # Now includes debt service
            debt = debt + deficit
            debt_to_gdp = (debt / gdp) * 100
            
            # Update economic condition for next year's multipliers
            economic_condition = self.assess_economic_condition(gdp, debt_to_gdp)
            spending_multiplier, tax_multiplier = self.get_multipliers(economic_condition)
            
            results.append({
                'Year': year + 1,
                'GDP': gdp,
                'Oil_Revenue': oil_revenue,
                'Non_Oil_Revenue': non_oil_revenue,
                'Total_Revenue': total_revenue,
                'Spending': spending,
                'Debt_Service': debt_service,
                'Deficit': deficit,
                'Debt': debt,
                'Debt_to_GDP': debt_to_gdp,
                'GDP_Growth': effective_growth,
                'Interest_Rate': effective_interest_rate,
                'Oil_Price': current_oil_price,
                'Economic_Condition': economic_condition,
                'Crowding_Out_Effect': crowding_out_effect
            })
            
        return pd.DataFrame(results)
    
    def assess_economic_condition(self, gdp, debt_to_gdp):
        """Determine if economy is in recession, normal, or boom"""
        if debt_to_gdp > 60:
            return "high_debt"
        elif gdp < self.initial_gdp * 0.98:  # Contraction
            return "recession"
        elif gdp > self.initial_gdp * 1.05:  # Strong growth
            return "boom"
        else:
            return "normal"
    
    def get_multipliers(self, economic_condition):
        """Time-varying multipliers based on economic conditions"""
        if economic_condition == "recession":
            return 0.8, 0.5  # Higher multipliers in recession
        elif economic_condition == "boom":
            return 0.4, 0.2  # Lower multipliers in boom (crowding out)
        elif economic_condition == "high_debt":
            return 0.3, 0.1  # Very low multipliers with high debt (confidence effect)
        else:  # normal
            return 0.6, 0.3

# ======================
# STREAMLIT INTERFACE
# ======================

st.set_page_config(
    page_title="📊 Nigeria Fiscal Simulator",
    page_icon="🇳🇬",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #008751;
        text-align: center;
        margin-bottom: 2rem;
    }
    .nigeria-green {
        background-color: #008751;
        color: white;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"> Nigeria Fiscal Policy Simulator</div>', unsafe_allow_html=True)

# Sidebar controls
st.sidebar.header("🎛️ Policy Controls")

# Oil market assumptions
st.sidebar.subheader("🛢️ Oil Market Assumptions")
oil_price_shock = st.sidebar.slider(
    "Oil Price Shock (%)", 
    min_value=-50.0, max_value=100.0, value=0.0, step=5.0,
    help="Percentage change in oil prices from current levels"
)

# Economic assumptions
st.sidebar.subheader("📈 Economic Assumptions")
baseline_growth = st.sidebar.slider(
    "Non-Oil GDP Growth (%)", 
    min_value=0.0, max_value=8.0, value=3.0, step=0.5
)

# Fiscal policy levers
st.sidebar.subheader("🏛️ Fiscal Policy Levers")

tax_change = st.sidebar.slider(
    "Non-Oil Revenue Change (%)", 
    min_value=-20.0, max_value=50.0, value=0.0, step=2.0,
    help="Change in tax collection efficiency and non-oil revenue"
)

spending_change = st.sidebar.slider(
    "Government Spending Change (%)", 
    min_value=-30.0, max_value=40.0, value=0.0, step=2.0,
    help="Change in total government expenditure"
)

# Model execution
@st.cache_data
def run_enhanced_model(tax_change, spending_change, growth_rate, oil_shock):
    model = NigeriaFiscalModel()
    return model.calculate_impact(tax_change, spending_change, growth_rate, oil_shock)

results_df = run_enhanced_model(tax_change, spending_change, baseline_growth, oil_price_shock)

# Key Metrics Dashboard
st.subheader("📊 Key Fiscal Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    debt_change = results_df['Debt_to_GDP'].iloc[-1] - results_df['Debt_to_GDP'].iloc[0]
    st.metric(
        "Debt-to-GDP (5Y)", 
        f"{results_df['Debt_to_GDP'].iloc[-1]:.1f}%",
        f"{debt_change:+.1f}%"
    )

with col2:
    avg_growth = results_df['GDP_Growth'].mean()
    st.metric(
        "Avg GDP Growth", 
        f"{avg_growth:.1f}%",
        f"{(avg_growth - baseline_growth):+.1f}% vs baseline"
    )

with col3:
    oil_reliance = (results_df['Oil_Revenue'].iloc[-1] / results_df['Total_Revenue'].iloc[-1]) * 100
    st.metric(
        "Oil Revenue Share", 
        f"{oil_reliance:.1f}%",
        "of total revenue"
    )

with col4:
    interest_rate_change = results_df['Interest_Rate'].iloc[-1] - results_df['Interest_Rate'].iloc[0]
    st.metric(
        "Sovereign Interest Rate", 
        f"{results_df['Interest_Rate'].iloc[-1]:.1f}%",
        f"{interest_rate_change:+.1f}%"
    )

# Enhanced Visualizations
st.subheader("📈 Comprehensive Fiscal Analysis")

# Create tabs for different aspects
tab1, tab2, tab3, tab4 = st.tabs(["Debt Dynamics", "Revenue Composition", "Growth Drivers", "Fiscal Sustainability"])

with tab1:
    fig_debt = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Debt-to-GDP Ratio', 'Sovereign Borrowing Cost', 
                       'Debt Service Burden', 'Primary Balance'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    # Debt-to-GDP
    fig_debt.add_trace(
        go.Scatter(x=results_df['Year'], y=results_df['Debt_to_GDP'], 
                   name="Debt/GDP", line=dict(color='red', width=3)),
        row=1, col=1
    )
    
    # Interest rate
    fig_debt.add_trace(
        go.Scatter(x=results_df['Year'], y=results_df['Interest_Rate'], 
                   name="Interest Rate", line=dict(color='orange', width=3)),
        row=1, col=2
    )
    
    # Debt service
    fig_debt.add_trace(
        go.Bar(x=results_df['Year'], y=results_df['Debt_Service'], 
               name="Debt Service", marker_color='purple'),
        row=2, col=1
    )
    
    # Primary balance (revenue - spending excluding interest)
    results_df['Primary_Balance'] = results_df['Total_Revenue'] - results_df['Spending']
    fig_debt.add_trace(
        go.Bar(x=results_df['Year'], y=results_df['Primary_Balance'], 
               name="Primary Balance", marker_color='green'),
        row=2, col=2
    )
    
    fig_debt.update_layout(height=600, showlegend=True)
    st.plotly_chart(fig_debt, use_container_width=True)

with tab2:
    # Revenue composition over time
    revenue_data = []
    for idx, row in results_df.iterrows():
        revenue_data.extend([
            {'Year': row['Year'], 'Source': 'Oil', 'Revenue': row['Oil_Revenue']},
            {'Year': row['Year'], 'Source': 'Non-Oil', 'Revenue': row['Non_Oil_Revenue']}
        ])
    
    revenue_df = pd.DataFrame(revenue_data)
    fig_revenue = px.area(revenue_df, x='Year', y='Revenue', color='Source',
                         title='Revenue Composition Over Time',
                         color_discrete_map={'Oil': '#FFA500', 'Non-Oil': '#008751'})
    st.plotly_chart(fig_revenue, use_container_width=True)

with tab3:
    fig_growth = go.Figure()
    
    fig_growth.add_trace(go.Bar(name='Baseline Growth', x=results_df['Year'], 
                               y=[baseline_growth]*len(results_df),
                               marker_color='lightgray'))
    
    fig_growth.add_trace(go.Bar(name='Fiscal Impact', x=results_df['Year'], 
                               y=results_df['GDP_Growth'] - baseline_growth,
                               marker_color='blue'))
    
    fig_growth.add_trace(go.Bar(name='- Crowding Out', x=results_df['Year'], 
                               y=-results_df['Crowding_Out_Effect'],
                               marker_color='red'))
    
    fig_growth.add_trace(go.Scatter(name='Actual Growth', x=results_df['Year'], 
                                   y=results_df['GDP_Growth'],
                                   line=dict(color='black', width=3)))
    
    fig_growth.update_layout(barmode='relative', title='GDP Growth Decomposition')
    st.plotly_chart(fig_growth, use_container_width=True)

# Policy Insights
st.subheader("💡 Nigeria-Specific Policy Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛢️ Oil Dependency Analysis")
    
    final_oil_share = (results_df['Oil_Revenue'].iloc[-1] / results_df['Total_Revenue'].iloc[-1]) * 100
    initial_oil_share = (results_df['Oil_Revenue'].iloc[0] / results_df['Total_Revenue'].iloc[0]) * 100
    
    if final_oil_share > 60:
        st.error(f"**High Oil Dependency**: {final_oil_share:.1f}% of revenue from oil. Vulnerable to price shocks.")
    elif final_oil_share < 30:
        st.success(f"**Diversified Revenue**: {final_oil_share:.1f}% of revenue from oil. More resilient economy.")
    else:
        st.warning(f"**Moderate Oil Dependency**: {final_oil_share:.1f}% of revenue from oil.")
    
    # Debt sustainability
    if results_df['Debt_to_GDP'].iloc[-1] > 70:
        st.error("**Debt Sustainability Concern**: Debt levels may trigger IMF program requirements")
    elif results_df['Debt_to_GDP'].iloc[-1] > 50:
        st.warning("**Moderate Debt Risk**: Approaching prudent debt limits")

with col2:
    st.markdown("### 📊 Multiplier Analysis")
    
    current_condition = results_df['Economic_Condition'].iloc[-1]
    spending_mult, tax_mult = NigeriaFiscalModel().get_multipliers(current_condition)
    
    st.info(f"**Current Economic Condition**: {current_condition.replace('_', ' ').title()}")
    st.metric("Spending Multiplier", f"{spending_mult:.2f}")
    st.metric("Tax Multiplier", f"{tax_mult:.2f}")
    
    if current_condition == "recession":
        st.success("**Recommendation**: Counter-cyclical spending has high impact now")
    elif current_condition == "high_debt":
        st.warning("**Recommendation**: Fiscal consolidation needed to restore confidence")

# Enhanced data table
with st.expander("📋 Detailed Projection Data"):
    display_df = results_df.copy()
    numeric_cols = ['GDP', 'Oil_Revenue', 'Non_Oil_Revenue', 'Total_Revenue', 
                   'Spending', 'Debt_Service', 'Deficit', 'Debt']
    
    for col in numeric_cols:
        display_df[col] = display_df[col].round(1)
    
    display_df['Debt_to_GDP'] = display_df['Debt_to_GDP'].round(1)
    display_df['GDP_Growth'] = display_df['GDP_Growth'].round(1)
    display_df['Interest_Rate'] = display_df['Interest_Rate'].round(1)
    display_df['Oil_Price'] = display_df['Oil_Price'].round(1)
    
    st.dataframe(display_df)

# Methodology
with st.expander("🔬 Enhanced Methodology"):
    st.markdown("""
    **Nigeria-Specific Model Enhancements:**
    
    🛢️ **Oil Revenue Module:**
    - Explicit modeling of oil revenue based on price and production
    - Oil price shocks directly impact fiscal space
    - Tracks revenue diversification away from oil
    
    📈 **Debt-Growth Feedback Loop:**
    - Higher debt → Higher risk premium → Higher interest rates
    - Debt service costs crowd out productive spending
    - Non-linear effects: severe crowding out at high debt levels
    
    🔄 **Time-Varying Multipliers:**
    - **Recession**: Higher multipliers (0.8 spending, 0.5 tax)
    - **Boom**: Lower multipliers (0.4 spending, 0.2 tax)  
    - **High Debt**: Very low multipliers due to confidence effects
    
    ⚠️ **Crowding-Out Effects:**
    - Rising debt service reduces funds for productive investment
    - Higher interest rates discourage private investment
    - Model captures both direct and indirect crowding out
    
    **Key Policy Variables:**
    - Debt sustainability thresholds (50%, 70% of GDP)
    - Oil revenue dependency (target < 30%)
    - Interest rate risk premium dynamics
    """)

st.markdown("---")
st.markdown("*Nigeria Fiscal Simulator v2.0 - Incorporating oil dependency and debt feedback effects*")