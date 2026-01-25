import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'DataFellas - ResTech 2026',
  description: 'Workflow Orchestrator untuk Automasi Riset Kualitatif',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="id">
      <body>{children}</body>
    </html>
  )
}
