import React from 'react';

const ClassificationReport = ({ data }) => {
  const rows = ['Hate Speech', 'Offensive Language', 'Neither'];
  const metrics = ['precision', 'recall', 'f1-score', 'support'];

  const formatNumber = (num) => typeof num === 'number' ? num.toFixed(3) : num;

  return (
    <div className="p-4 max-w-4xl mx-auto bg-[#242424] rounded-2xl shadow">
      <h2 className="text-xl font-semibold mb-4 text-center">Classification Report</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full text-sm text-center border border-gray-300">
          <thead className="bg-[#242424]">
            <tr>
              <th className="px-4 py-2 border">Label</th>
              {metrics.map(metric => (
                <th key={metric} className="px-4 py-2 border capitalize">{metric}</th>
              ))}
            </tr>
          </thead>
          <tbody>
                {rows.map(label => {
                const entry = data[label];
                return (
                    <tr key={label}>
                    <td className="px-4 py-2 border font-medium">{label}</td>
                    {metrics.map(metric => (
                        <td key={metric} className="px-4 py-2 border">
                        {entry && entry[metric] !== undefined ? formatNumber(entry[metric]) : '—'}
                        </td>
                    ))}
                    </tr>
                );
                })}
            <tr className="bg-[#242424]">
              <td className="px-4 py-2 border font-semibold">Accuracy</td>
              <td className="px-4 py-2 border" colSpan={3}>{(data.accuracy * 100).toFixed(2)}%</td>
            </tr>
            {['macro avg', 'weighted avg'].map(avg => (
              <tr key={avg}>
                <td className="px-4 py-2 border font-medium capitalize">{avg}</td>
                {metrics.map(metric => (
                  <td key={metric} className="px-4 py-2 border">
                    {formatNumber(data[avg][metric])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ClassificationReport;
